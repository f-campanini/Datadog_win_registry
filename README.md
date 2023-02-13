# Datadog_win_registry
A custom check that allows to read registry keys and provide custom metrics from it

## Installation
Copy the python script in the `checks.d` folder and the yaml file in the `conf.d` of the Datadog config hierarchy (typically in `%PROGRAMDATA%\Datadog`).
The resulting hierarchy should be:

```
%PROGRAMDATA%\Datadog
├── checks.d
│   └── custom_win_reg.py
└── conf.d
    └── custom_win_reg.yaml

```
See [the custom check documentation](https://docs.datadoghq.com/developers/write_agent_check/?tab=agentv6v7) for more information.

Install the library winregistry using the below command:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\embedded3\python" -m pip install winregistry
```

## Configuration

The conf.yaml file should be placed under the conf.d folder in the Datadog config hierarchy.

### cutom_win_reg.yaml description

Configuration example
```yaml
  - registry_key: ssl3.client
    min_collection_interval: 120
    key_path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL\ 3.0\Client
    key_name: Enabled
    metric_name: win.registry.ssl3.client.enabled
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
