def system_boot_time():
    '''
    Get the system boot time.

    CLI Example::

        salt 'os:Windows' sccm.system_boot_time
    '''
    return __salt__['cmd.run']('systeminfo | select-string "System Boot Time"', shell='powershell')

def hardware_inventory():
    '''
    Invoke the hardware inventory cycle

    CLI Example::

        salt 'os:Windows' sccm.hardware_inventory
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000001}"', shell='powershell')

def software_inventory():
    '''
    Invoke the software inventory cycle

    CLI Example::

        salt 'os:Windows' sccm.software_inventory
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000002}"', shell='powershell')

def discovery_data_record():
    '''
    Invoke the discovery data record

    CLI Example::

        salt 'os:Windows' sccm.discovery_data_record
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000003}"', shell='powershell')

def request_machine_policy():
    '''
    Request the machine policy

    CLI Example::

        salt 'os:Windows' sccm.request_machine_policy
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000021}"', shell='powershell')

def evaluate_machine_policy():
    '''
    Evaluate the machine policy

    CLI Example::

        salt 'os:Windows' sccm.evaluate_machine_policy
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000022}"', shell='powershell')

def file_collection():
    '''
    Invoke file collection cycle

    CLI Example::

        salt 'os:Windows' sccm.file_collection
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000010}"', shell='powershell')

def sw_metering_usage_report():
    '''
    Software metering generating usage report

    CLI Example::

        salt 'os:Windows' sccm.sw_metering_usage_report
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000031}"', shell='powershell')

def windows_installer_source_list():
    '''
    Windows installer source list

    CLI Example::

        salt 'os:Windows' sccm.windows_installer_source_list
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000032}"', shell='powershell')

def software_updates_scan():
    '''
    Invoke software updates scan

    CLI Example::

        salt 'os:Windows' sccm.software_updates_scan
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000113}"', shell='powershell')

def software_updates_store():
    '''
    Invoke software updates store

    CLI Example::

        salt 'os:Windows' sccm.software_updates_store
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000114}"', shell='powershell')

def software_updates_deployment():
    '''
    Invoke software updates deployment

    CLI Example::

        salt 'os:Windows' sccm.software_updates_deployment
    '''
    return __salt__['cmd.run']('Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name TriggerSchedule -ArgumentList "{00000000-0000-0000-0000-000000000108}"', shell='powershell')

def update_count():
    '''
    Get the number of available updates from ConfigMgr

    CLI Example::

        salt 'os:Windows' sccm.update_count
    '''
    return __salt__['cmd.run']('(gcim -namespace root\ccm\clientsdk -query \'Select * from CCM_SoftwareUpdate\' | measure-object).Count', shell='powershell')

def list_updates():
    '''
    Get the list of available updates

    CLI Example::

        salt 'os:Windows' sccm.updates
    '''
    return __salt__['cmd.run']('gcim -namespace root\ccm\clientsdk -query \'Select * from CCM_SoftwareUpdate\'', shell="powershell")

def install_updates():
    '''
    Install updates with deadlines

    CLI Example::

        salt 'os:Windows' sccm.install_updates
    '''
    return __salt__['cmd.run']('iwmi -namespace root\ccm\clientsdk -Class CCM_SoftwareUpdatesManager -name InstallUpdates([System.Management.MangementObject[]](gwmi -namespace root\ccm\clientsdk -query \'Select * from CCM_SoftwareUpdate\'))', shell='powershell')

def reboot_pending():
    '''
    Is a reboot pending from ConfigMgr

    CLI Example::

        salt 'os:Windows' sccm.reboot_pending
    '''
    return __salt__['cmd.run']('(icim -namespace root\ccm\clientsdk -ClassName CCM_ClientUtilities -Name DetermineIfRebootPending).RebootPending', shell='powershell')
