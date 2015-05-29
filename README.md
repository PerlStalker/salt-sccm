salt-sccm
=========

Some basic commands to invoke System Center Configuration Manager client actions.

Drop sccm.py in /srv/salt/_modules and run saltutil.sync_module or
saltutil.sync_all to push the module to the clients.

* sccm.system_boot_type - get the system boot time
* sccm.update_count - get the number of availale updates
* sccm.list_updates - get the list of available updates
* sccm.install_updates - install the updates with a deadline set
* sccm.reboot_pending - is there a reboot pending
* sccm.hardware_inventory - start the hardware inventory cycle
* sccm.software_inventory - start the software inventory cycle
* sccm.request_machine_policy - request the machine policy
* sccm.evaluate_machine_policy - evaluate the machine policy
* sccm.file_collection - invoke the file collection cycle
* sccm.software_updates_scan - invoke the software updates scan
* sccm.software_updates_deployment - invoke the software updates deployment
