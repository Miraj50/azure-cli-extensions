Describe 'Azure Policy Testing' {
    BeforeAll {
        $extensionType = "microsoft.policyinsights"
        $extensionName = "policy"
        $extensionAgentName = "azure-policy"
        $extensionAgentNamespace = "kube-system"
        
        . $PSScriptRoot/../../helper/Constants.ps1
        . $PSScriptRoot/../../helper/Helper.ps1
    }

    It 'Creates the extension and checks that it onboards correctly' {
        Invoke-Expression "az $Env:K8sExtensionName create -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters --extension-type $extensionType -n $extensionName --no-wait" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty        

        $output = Invoke-Expression "az $Env:K8sExtensionName show -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters -n $extensionName" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty

        $isAutoUpgradeMinorVersion = ($output | ConvertFrom-Json).autoUpgradeMinorVersion 
        $isAutoUpgradeMinorVersion.ToString() -eq "True" | Should -BeTrue

        # Check that we get the principal id back for the created identity
        $principalId = ($output | ConvertFrom-Json).identity.principalId
        $principalId | Should -Not -BeNullOrEmpty

        # Loop and retry until the extension installs
        $n = 0
        do 
        {
            # Only check the extension config, not the pod since this doesn't bring up pods
            $output = Invoke-Expression "az $Env:K8sExtensionName show -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters -n $extensionName" -ErrorVariable badOut
            if (Has-ExtensionData $extensionName){
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Performs a show on the extension" {
        $output = Invoke-Expression "az $Env:K8sExtensionName show -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters -n $extensionName" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty
        $output | Should -Not -BeNullOrEmpty
    }

    It "Lists the extensions on the cluster" {
        $output = Invoke-Expression "az $Env:K8sExtensionName list -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty

        $output | Should -Not -BeNullOrEmpty
        $extensionExists = $output | ConvertFrom-Json | Where-Object { $_.extensionType -eq $extensionType }
        $extensionExists | Should -Not -BeNullOrEmpty
    }

    It "Deletes the extension from the cluster" {
        $output = Invoke-Expression "az $Env:K8sExtensionName delete -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters -n $extensionName --force" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty

        # Extension should not be found on the cluster
        $output = Invoke-Expression "az $Env:K8sExtensionName show -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters -n $extensionName" -ErrorVariable badOut
        $badOut | Should -Not -BeNullOrEmpty
        $output | Should -BeNullOrEmpty
    }

    It "Performs another list after the delete" {
        $output = Invoke-Expression "az $Env:K8sExtensionName list -c $($ENVCONFIG.arcClusterName) -g $($ENVCONFIG.resourceGroup) --cluster-type connectedClusters" -ErrorVariable badOut
        $badOut | Should -BeNullOrEmpty
        $output | Should -Not -BeNullOrEmpty
        
        $extensionExists = $output | ConvertFrom-Json | Where-Object { $_.extensionType -eq $extensionName }
        $extensionExists | Should -BeNullOrEmpty
    }
}
