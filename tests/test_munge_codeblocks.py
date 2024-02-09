import pytest
from convert.munge import process_code_blocks


code_block_1 = """This is a code_block:

    describe aws_shield_subscription do

"""

code_block_1_output = """This is a code_block:

```
describe aws_shield_subscription do
```

"""



code_block_2 = """This is a code_block:

    describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
        it { should exist }
    end

"""

code_block_2_output = """This is a code_block:

```
describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
    it { should exist }
end
```

"""

code_block_3="""## Syntax

Ensure that an `aws_ec2_dhcp_option` exists

    describe aws_ec2_dhcp_option('dopt-0123456789abcdefg') do
      it { should exist }
    end

    describe aws_ec2_dhcp_option(dhcp_options_id: 'dopt-0123456789abcdefg') do
      it { should exist }
    end

    describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
        it { should exist }
    end

#### Parameters
This resource accepts a one of the below mentioned parameters

"""

code_block_3_output = """## Syntax

Ensure that an `aws_ec2_dhcp_option` exists

```
describe aws_ec2_dhcp_option('dopt-0123456789abcdefg') do
  it { should exist }
end
```

```
describe aws_ec2_dhcp_option(dhcp_options_id: 'dopt-0123456789abcdefg') do
  it { should exist }
end
```

```
describe aws_ec2_dhcp_option(name: 'dopt-vpc-1') do
    it { should exist }
end
```

#### Parameters
This resource accepts a one of the below mentioned parameters

"""

code_block_4 = '''
some text

```
  azure_active_directory_objects.values.each do |value|
    describe azure_active_directory_object(id: value)  do
      it { should exist }
      its('visibility') { should_not be_empty }
    end
  end

```

more text

'''

code_block_5="""

#### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

    describe aws_config_delivery_channel('my_channel') do
      it { should exist }
    end

    describe aws_config_delivery_channel('my-nonexistent-channel') do
      it { should_not exist }
    end
## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

You can find detailed documentation at [Actions, Resources, and Condition Keys for AWS Config](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsconfig.html).

"""

code_block_5_output = """

#### exist

The control will pass if the describe returns at least one result.

Use `should_not` to test the entity should not exist.

```
describe aws_config_delivery_channel('my_channel') do
  it { should exist }
end
```

```
describe aws_config_delivery_channel('my-nonexistent-channel') do
  it { should_not exist }
end
```
## AWS Permissions

Your [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) will need the `ConfigService:Client:DescribeDeliveryChannelsResponse` action with Effect set to Allow.

You can find detailed documentation at [Actions, Resources, and Condition Keys for AWS Config](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsconfig.html).

"""

code_block_6 = '''
### exist

The control will pass if the describe returns at least one result.

      it { should exist }

'''

code_block_6_output = '''
### exist

The control will pass if the describe returns at least one result.

```
it { should exist }
```

'''

code_block_7 = """
### Install Chef Node Management Agent using a Powershell install script

You can install Chef Node Management Agent by downloading and executing the installation script:

    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://chef-platform-content.s3.us-east-2.amazonaws.com/install.ps1'))
"""

code_block_7_output = """
### Install Chef Node Management Agent using a Powershell install script

You can install Chef Node Management Agent by downloading and executing the installation script:

```
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://chef-platform-content.s3.us-east-2.amazonaws.com/install.ps1'))
```
"""

code_block_8 ="""
3.  The installer uses `/var/lib/kurl/` to store temporary data during the install process. If you need to override this temporary directory path you can add `kurl-install-directory=/path/to/dir/` as an additional install argument and it will be suffixed with `/kurl/` and used as the temporary directory that can be removed after installation is complete. The directory must be writable by the user running the install command. The partition this directory exists in is required to have 8GB of free space available.

    Here is an example install command that overrides the temporary install data path:

        curl -sSL https://kurl.sh/XXXXX-XXXXX-XXXXXX | sudo bash -s ha kurl-install-directory=/path/to/dir/

    The installer runs a series of preflight checks to ensure that the node is ready for installation. If any of the preflight checks fail, the installer exits so that the issues can be resolved. In a non-production environment, you can ignore the failing preflight checks and install anyway. To do this, add `host-preflight-ignore` as an additional install argument, for example:

    Copy

        curl -sSL https://kurl.sh/XXXXX-XXXXX-XXXXXX | sudo bash -s ha host-preflight-ignore

    If you need to override any installer settings you must specify the installer override patch file with the installer command. See <a href="Overriding-Chef-Platform-Manager-Settings_2872311863.html" data-linked-resource-id="2872311863" data-linked-resource-version="3" data-linked-resource-type="page">Overriding Chef Platform Manager Settings</a> for more information.

    You may be prompted to disable anything on the system that is incompatible. Respond with **Y** to disable and continue with the installation.

    When prompted to enter the load balancer address use the Kubernetes API load balancer IP/FQDN in lowercase and specify port 6443, for example, `foo.bar:6443`.

Be aware that the installation can take 30 minutes or more to complete.
"""

code_block_8_output = """
3.  The installer uses `/var/lib/kurl/` to store temporary data during the install process. If you need to override this temporary directory path you can add `kurl-install-directory=/path/to/dir/` as an additional install argument and it will be suffixed with `/kurl/` and used as the temporary directory that can be removed after installation is complete. The directory must be writable by the user running the install command. The partition this directory exists in is required to have 8GB of free space available.

    Here is an example install command that overrides the temporary install data path:

    ```
    curl -sSL https://kurl.sh/XXXXX-XXXXX-XXXXXX | sudo bash -s ha kurl-install-directory=/path/to/dir/
    ```

    The installer runs a series of preflight checks to ensure that the node is ready for installation. If any of the preflight checks fail, the installer exits so that the issues can be resolved. In a non-production environment, you can ignore the failing preflight checks and install anyway. To do this, add `host-preflight-ignore` as an additional install argument, for example:

    Copy

    ```
    curl -sSL https://kurl.sh/XXXXX-XXXXX-XXXXXX | sudo bash -s ha host-preflight-ignore
    ```

    If you need to override any installer settings you must specify the installer override patch file with the installer command. See <a href="Overriding-Chef-Platform-Manager-Settings_2872311863.html" data-linked-resource-id="2872311863" data-linked-resource-version="3" data-linked-resource-type="page">Overriding Chef Platform Manager Settings</a> for more information.

    You may be prompted to disable anything on the system that is incompatible. Respond with **Y** to disable and continue with the installation.

    When prompted to enter the load balancer address use the Kubernetes API load balancer IP/FQDN in lowercase and specify port 6443, for example, `foo.bar:6443`.

Be aware that the installation can take 30 minutes or more to complete.
"""

def test_code_blocks():
    assert process_code_blocks(code_block_1) == code_block_1_output
    assert process_code_blocks(code_block_2) == code_block_2_output
    assert process_code_blocks(code_block_3) == code_block_3_output
    assert process_code_blocks(code_block_5) == code_block_5_output
    assert process_code_blocks(code_block_6) == code_block_6_output

def test_code_blocks_end_of_page():
    assert process_code_blocks(code_block_7) == code_block_7_output


def test_code_blocks_without_changes():
    assert process_code_blocks(code_block_4) == code_block_4

# def test_code_blocks_in_lists():
#     assert process_code_blocks(code_block_8) == code_block_8_output
