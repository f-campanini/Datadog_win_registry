# Datadog_win_registry
A custom check that allows to read registry keys and provide custom metrics from it

## Installation
Copy the python script in the checks.d folder in the Datadog config hierarchy.

Install the library winregistry using the below command:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\embedded3\python" -m pip install winregistry
```

## Configuration

The conf.yaml file should be placed in a directory named as the check (winreg_check.d) under the conf.d folder in the Datadog config hierarchy.

### conf.yaml description

Configuration example
```yaml
  - registry_key: ssl3.client
    min_collection_interval: 120
    key_path: "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\SSL\ 3.0\\Client"
    key_name: "Enabled"
    metric_name: "win.registry.ssl3.client.enabled"
    tags:
      - tag1:'string'
      - tag2:'25'
```

## Useful commands in the Windows env

### to open the Datadog agent gui
```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" launch-gui
```

### to check the status of the agent
```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" status
```