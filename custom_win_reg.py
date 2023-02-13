
# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

from winregistry import WinRegistry

class Winreg_Check(AgentCheck):
    def check(self, instance):

        local_reg_path = instance['key_path']
        local_reg_name = instance['key_name']
        local_metric_name = instance['metric_name']
 
        with WinRegistry() as client:
            test_entry = client.read_entry(local_reg_path, local_reg_name)

        #Send the metric to Datadog
        self.gauge(local_metric_name, test_entry.value, tags=self.instance.get('tags', []))