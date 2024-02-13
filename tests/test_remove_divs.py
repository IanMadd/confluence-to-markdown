import pytest
from convert.munge import *

input_string_1 = """
<div id="page">

<div id="main" class="aui-page-panel">

<div id="main-header">



</div>

<div id="content" class="view">

<div id="main-content" class="wiki-content group">

A node that has agents installed for performing actions. Example : Node Management Client , Courier Runner, or agent like skills such as Infra Client, Inspec Client, etc

</div>

</div>

</div>

</div>

"""

output_string_1 = """
A node that has agents installed for performing actions. Example : Node Management Client , Courier Runner, or agent like skills such as Infra Client, Inspec Client, etc

"""

def test_remove_divs_1():
    assert remove_divs(input_string_1) == output_string_1


input_string_2 = """

# A

- <div>

  <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  </div>

  <div class="details">

  [Action](/courier/action/) <span class="smalltext">— the fact or process of doing something, typically to achieve an aim.</span>
  see also:

  - [Job Action](/courier/job_action_courier/)

  </div>

- <div>

  <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  </div>

  <div class="details">

  [Ad-hoc](/courier/ad_hoc/) <span class="smalltext">— An ad hoc activity is not planned in advance, but is done or formed only because a particular situation has made it necessary. There, the focus is on quick delivery and solving a specific problem rather.</span>
  see also

  - [Courier Ad-hoc Job](/courier/job_courier_ad_hoc/)

  </div>
"""

output_string_2 = """

# A

- <span class="icon aui-icon content-type-page" title="Page">Page:</span>

    [Action](/courier/action/) <span class="smalltext">— the fact or process of doing something, typically to achieve an aim.</span>
  see also:

  - [Job Action](/courier/job_action_courier/)

  - <span class="icon aui-icon content-type-page" title="Page">Page:</span>

    [Ad-hoc](/courier/ad_hoc/) <span class="smalltext">— An ad hoc activity is not planned in advance, but is done or formed only because a particular situation has made it necessary. There, the focus is on quick delivery and solving a specific problem rather.</span>
  see also

  - [Courier Ad-hoc Job](/courier/job_courier_ad_hoc/)

  
"""

def test_remove_divs_2():
    assert remove_divs(input_string_2) == output_string_2


input_string_3="""
- <div>

  <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  </div>
"""

output_string_3 = """
- <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  """

def test_remove_divs_3():
  assert remove_divs(input_string_3) == output_string_3


input_string_4 = """
<div class="pageSection group">

<div class="pageSectionHeader">
"""

output_string_4 = """
"""

def test_remove_divs_4():
  assert remove_divs(input_string_4) == output_string_4


input_string_5 = """


<div id="page">

<div id="main" class="aui-page-panel">

<div id="main-header">



</div>

<div id="content" class="view">

<div id="main-content" class="wiki-content group">

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

**Important!** This topic provides instructions on how to create a High Availability (HA) cluster and assumes you have already run the Chef Platform Manager on the first node. Please see [Install Into an Embedded Kubernetes Cluster](/courier/install_on_an_embedded_kubernetes_cluster/) if you have not yet installed on the first node.

</div>

</div>

### HA considerations

- HA clusters require at least 3 nodes and the total number of nodes must be an odd number.

- Only one PostgreSQL pod can run on a node. For example, you need 3 nodes in a cluster if you want to go to 3 PostgreSQL pods to enable a replica set.

- The first node that the initial install is running on should be in the target group to start. The additional nodes should only be added to the target groups after they’ve been joined to the cluster.

To add additional nodes to a cluster:

1.  From the Chef Platform Manager UI, click the Cluster Management tab.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082604.png?width=760" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082604.png" data-height="452" data-width="828" data-unresolved-comment-count="0" data-linked-resource-id="2872082604" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205254.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="26f93266-c6e4-4bd9-a744-b7f5481594f6" data-media-type="file" width="760" /></span>

The Cluster Management page displays your installed nodes.

2.  Click **Add a node**.

3.  Under Add a Node, ensure that you have selected **Master Node** and then click **Copy command**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872246413.png?width=760" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872246413.png" data-height="842" data-width="2000" data-unresolved-comment-count="0" data-linked-resource-id="2872246413" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205332.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="fcc0998f-ba14-4b9d-98da-f3f18a9b3403" data-media-type="file" width="760" /></span>

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

**Important!** The code generated here expires after time. Progress Chef recommends that you always copy the code as you work to add additional nodes. Do not save the code for use later.

</div>

</div>

4.  Go to your Command-Line Interface (CLI) and paste the copied command for your additional nodes.

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**Note:** You can add multiple nodes simultaneously.

</div>

</div>

If your environment requires a proxy then the `additionalNoProxyAddresses` override option must include an IP range in CIDR notation that encompasses the new node's private IP. If it does not then you will need to update the installer override file to add the new node's private IP to the `additionalNoProxyAddresses` list and specify the override file when running the join node command on the new node, and then re-run the install command on *every other node* with the installer override file specified. Failure to ensure that all nodes have the updated `additionalNoProxyAddresses` list will result in cluster networking issues and issues with Chef Platform. See the [Define Proxy Settings](/courier/define_proxy_settings/) topic for more information on specifying proxy settings.

5.  Back in the Chef Platform Manager UI, click the Application tab, and then click **Config**.

<div class="confluence-information-macro confluence-information-macro-note">

<span class="aui-icon aui-icon-small aui-iconfont-warning confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

EVERYTHING BELOW HERE MAY CHANGE WE DO NOT HAVE THE CONFIG ITEMS DONE YET

</div>

</div>

6.  Scroll down to the heading **HA Settings**. Select **HA Environment** and click **Save config**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082619.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082619.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872082619" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205622.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="06df3d66-7137-43b4-a96d-d8d48baac8df" data-media-type="file" width="218" /></span>

7.  Once you save the new configuration, you are prompted to view the new version. Click **Go to new version**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872311879.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872311879.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872311879" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205627.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="5c8c5592-2e73-4751-af86-e9c43cbbd345" data-media-type="file" width="218" /></span>

8.  On Version History, click **Deploy**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082619.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082619.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872082619" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205622.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="06df3d66-7137-43b4-a96d-d8d48baac8df" data-media-type="file" width="218" /></span>

9.  Return to the Application tab. Once the Application Status is *Ready* you have added the additional nodes to your Chef Platform HA environment.

10. Add the new nodes to the load balancer target groups.

</div>

<div class="pageSection group">

<div class="pageSectionHeader">

## Attachments:
"""

output_string_5 = """


**Important!** This topic provides instructions on how to create a High Availability (HA) cluster and assumes you have already run the Chef Platform Manager on the first node. Please see [Install Into an Embedded Kubernetes Cluster](/courier/install_on_an_embedded_kubernetes_cluster/) if you have not yet installed on the first node.

### HA considerations

- HA clusters require at least 3 nodes and the total number of nodes must be an odd number.

- Only one PostgreSQL pod can run on a node. For example, you need 3 nodes in a cluster if you want to go to 3 PostgreSQL pods to enable a replica set.

- The first node that the initial install is running on should be in the target group to start. The additional nodes should only be added to the target groups after they’ve been joined to the cluster.

To add additional nodes to a cluster:

1.  From the Chef Platform Manager UI, click the Cluster Management tab.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082604.png?width=760" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082604.png" data-height="452" data-width="828" data-unresolved-comment-count="0" data-linked-resource-id="2872082604" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205254.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="26f93266-c6e4-4bd9-a744-b7f5481594f6" data-media-type="file" width="760" /></span>

The Cluster Management page displays your installed nodes.

2.  Click **Add a node**.

3.  Under Add a Node, ensure that you have selected **Master Node** and then click **Copy command**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872246413.png?width=760" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872246413.png" data-height="842" data-width="2000" data-unresolved-comment-count="0" data-linked-resource-id="2872246413" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205332.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="fcc0998f-ba14-4b9d-98da-f3f18a9b3403" data-media-type="file" width="760" /></span>

**Important!** The code generated here expires after time. Progress Chef recommends that you always copy the code as you work to add additional nodes. Do not save the code for use later.

4.  Go to your Command-Line Interface (CLI) and paste the copied command for your additional nodes.

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

**Note:** You can add multiple nodes simultaneously.

If your environment requires a proxy then the `additionalNoProxyAddresses` override option must include an IP range in CIDR notation that encompasses the new node's private IP. If it does not then you will need to update the installer override file to add the new node's private IP to the `additionalNoProxyAddresses` list and specify the override file when running the join node command on the new node, and then re-run the install command on *every other node* with the installer override file specified. Failure to ensure that all nodes have the updated `additionalNoProxyAddresses` list will result in cluster networking issues and issues with Chef Platform. See the [Define Proxy Settings](/courier/define_proxy_settings/) topic for more information on specifying proxy settings.

5.  Back in the Chef Platform Manager UI, click the Application tab, and then click **Config**.

<span class="aui-icon aui-icon-small aui-iconfont-warning confluence-information-macro-icon"></span>

EVERYTHING BELOW HERE MAY CHANGE WE DO NOT HAVE THE CONFIG ITEMS DONE YET

6.  Scroll down to the heading **HA Settings**. Select **HA Environment** and click **Save config**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082619.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082619.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872082619" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205622.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="06df3d66-7137-43b4-a96d-d8d48baac8df" data-media-type="file" width="218" /></span>

7.  Once you save the new configuration, you are prompted to view the new version. Click **Go to new version**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872311879.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872311879.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872311879" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205627.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="5c8c5592-2e73-4751-af86-e9c43cbbd345" data-media-type="file" width="218" /></span>

8.  On Version History, click **Deploy**.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="attachments/2871395501/2872082619.png?width=218" class="confluence-embedded-image image-center" loading="lazy" data-image-src="attachments/2871395501/2872082619.png" data-height="218" data-width="218" data-unresolved-comment-count="0" data-linked-resource-id="2872082619" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20240108-205622.png" data-base-url="https://chefio.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2871395501" data-linked-resource-container-version="4" data-media-id="06df3d66-7137-43b4-a96d-d8d48baac8df" data-media-type="file" width="218" /></span>

9.  Return to the Application tab. Once the Application Status is *Ready* you have added the additional nodes to your Chef Platform HA environment.

10. Add the new nodes to the load balancer target groups.

## Attachments:
"""

def test_remove_divs_5():
  assert remove_divs(input_string_5) == output_string_5
