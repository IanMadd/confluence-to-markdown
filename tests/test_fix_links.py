import pytest
from convert.munge import *

input_text_1 = """
see also:

- <a href="Job-Action%2C-Courier_2888859825.html" data-linked-resource-id="2888859825" data-linked-resource-version="3" data-linked-resource-type="page">Job Action</a>

</div>
"""

output_text_1 = """
see also:

- [Job Action](/courier/job_action_courier/)

</div>
"""

def test_fix_links_1():
    assert fix_links(input_text_1) == output_text_1


input_text_2 = """
see also:

- <a href="Job-Action%2C-Courier_2888859825.html" data-linked-resource-id="2888859825" data-linked-resource-version="3" data-linked-resource-type="page">Job Action</a>

see also:

<a href="Job-Action%2C-Courier_2888859825.html" data-linked-resource-id="2888859825" data-linked-resource-version="3" data-linked-resource-type="page">Job Action</a>

</div>
"""

output_text_2 = """
see also:

- [Job Action](/courier/job_action_courier/)

see also:

[Job Action](/courier/job_action_courier/)

</div>
"""

def test_fix_links_2():
    assert fix_links(input_text_2) == output_text_2


input_text_3 = """

<div id="content" class="view">

<div id="main-content" class="wiki-content group">

This will tie to first business scenario… <a href="https://chefio.atlassian.net/wiki/spaces/AR/pages/2885287994/Business+scenarios+for+Courier" data-linked-resource-id="2885287994" data-linked-resource-version="6" data-linked-resource-type="page">Business scenarios for Courier</a>

resources not yet included

1.  Whenever - Use Case: Demo on Scheduling Jobs --\>  <a href="https://urldefense.com/v3/__https:/youtu.be/0c-04be9Jr0__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekKHl6mCUQ$" class="external-link" rel="nofollow">Youtube Link</a>

2.  Wherever - Use Case: Demo on Controlled Rollout --\>  <a href="https://urldefense.com/v3/__https:/youtu.be/qYdhwPaBAbg__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekK5aYknHQ$" class="external-link" rel="nofollow">Youtube Link</a>

3.  Whatever - Use Case: Demo on Action Chaining --\> <a href="https://urldefense.com/v3/__https:/youtu.be/3ryqBtiAev8__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekIA0vKfUQ$" class="external-link" rel="nofollow">Youtube Link</a>

<a href="https://progresssoftware-my.sharepoint.com/personal/kjung_progress_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkjung%5Fprogress%5Fcom%2FDocuments%2FVideos%2FChef%2DCourier&amp;ct=1706814362522&amp;or=Teams%2DHL&amp;ga=1&amp;LOF=1" class="external-link" data-card-appearance="inline" rel="nofollow">https://progresssoftware-my.sharepoint.com/personal/kjung_progress_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkjung%5Fprogress%5Fcom%2FDocuments%2FVideos%2FChef%2DCourier&amp;ct=1706814362522&amp;or=Teams%2DHL&amp;ga=1&amp;LOF=1</a>

</div>
"""

output_text_3 = """

<div id="content" class="view">

<div id="main-content" class="wiki-content group">

This will tie to first business scenario… [Business scenarios for Courier](https://chefio.atlassian.net/wiki/spaces/AR/pages/2885287994/Business+scenarios+for+Courier)

resources not yet included

1.  Whenever - Use Case: Demo on Scheduling Jobs --\>  [Youtube Link](https://urldefense.com/v3/__https:/youtu.be/0c-04be9Jr0__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekKHl6mCUQ$)

2.  Wherever - Use Case: Demo on Controlled Rollout --\>  [Youtube Link](https://urldefense.com/v3/__https:/youtu.be/qYdhwPaBAbg__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekK5aYknHQ$)

3.  Whatever - Use Case: Demo on Action Chaining --\> [Youtube Link](https://urldefense.com/v3/__https:/youtu.be/3ryqBtiAev8__;!!JUyETn1neQ!5y1tbYnqCA1quDz-oigFLbd0EFo-5Y21xvkVIza_LWKRJIx_bY83dRViQbb_ohNETZErBUW11cJHbU_jruEwHfBfekIA0vKfUQ$)

[https://progresssoftware-my.sharepoint.com/personal/kjung_progress_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkjung%5Fprogress%5Fcom%2FDocuments%2FVideos%2FChef%2DCourier&amp;ct=1706814362522&amp;or=Teams%2DHL&amp;ga=1&amp;LOF=1](https://progresssoftware-my.sharepoint.com/personal/kjung_progress_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkjung%5Fprogress%5Fcom%2FDocuments%2FVideos%2FChef%2DCourier&amp;ct=1706814362522&amp;or=Teams%2DHL&amp;ga=1&amp;LOF=1)

</div>
"""

def test_fix_links_3():
    assert fix_links(input_text_3) == output_text_3


input_text_4 = """
<div class="panelContent" style="background-color: #EAE6FF;">

**Important!** This topic provides instructions on how to create a High Availability (HA) cluster and assumes you have already run the Chef Platform Manager on the first node. Please see <a href="Install-on-an-Embedded-Kubernetes-Cluster_2872246392.html" data-linked-resource-id="2872246392" data-linked-resource-version="1" data-linked-resource-type="page">Install Into an Embedded Kubernetes Cluster</a> if you have not yet installed on the first node.

</div>

If your environment requires a proxy then the `additionalNoProxyAddresses` override option must include an IP range in CIDR notation that encompasses the new node's private IP. If it does not then you will need to update the installer override file to add the new node's private IP to the `additionalNoProxyAddresses` list and specify the override file when running the join node command on the new node, and then re-run the install command on *every other node* with the installer override file specified. Failure to ensure that all nodes have the updated `additionalNoProxyAddresses` list will result in cluster networking issues and issues with Chef Platform. See the <a href="Define-Proxy-Settings_2872279174.html" data-linked-resource-id="2872279174" data-linked-resource-version="3" data-linked-resource-type="page">Define Proxy Settings</a> topic for more information on specifying proxy settings.

"""

output_text_4 = """
<div class="panelContent" style="background-color: #EAE6FF;">

**Important!** This topic provides instructions on how to create a High Availability (HA) cluster and assumes you have already run the Chef Platform Manager on the first node. Please see [Install Into an Embedded Kubernetes Cluster](/courier/install_on_an_embedded_kubernetes_cluster/) if you have not yet installed on the first node.

</div>

If your environment requires a proxy then the `additionalNoProxyAddresses` override option must include an IP range in CIDR notation that encompasses the new node's private IP. If it does not then you will need to update the installer override file to add the new node's private IP to the `additionalNoProxyAddresses` list and specify the override file when running the join node command on the new node, and then re-run the install command on *every other node* with the installer override file specified. Failure to ensure that all nodes have the updated `additionalNoProxyAddresses` list will result in cluster networking issues and issues with Chef Platform. See the [Define Proxy Settings](/courier/define_proxy_settings/) topic for more information on specifying proxy settings.

"""

def test_fix_links_4():
    assert fix_links(input_text_4) == output_text_4


input_text_5 = """

- <div>

  <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  </div>

  <div class="details">

  <a href="/wiki/spaces/Courier/pages/2889089219/Action" data-linked-resource-id="2889089219" data-linked-resource-type="page" data-linked-resource-version="2">Action</a> <span class="smalltext">— the fact or process of doing something, typically to achieve an aim.</span>
  see also:

  - <a href="/wiki/spaces/Courier/pages/2888859825/Job+Action%2C+Courier" data-linked-resource-id="2888859825" data-linked-resource-version="3" data-linked-resource-type="page">Job Action</a>

  </div>

- <div>

  <span class="icon aui-icon content-type-page" title="Page">Page:</span>

  </div>

  <div class="details">

  <a href="/wiki/spaces/Courier/pages/2888925476/Ad-hoc" data-linked-resource-id="2888925476" data-linked-resource-type="page" data-linked-resource-version="1">Ad-hoc</a> <span class="smalltext">— An ad hoc activity is not planned in advance, but is done or formed only because a particular situation has made it necessary. There, the focus is on quick delivery and solving a specific problem rather.</span>
  see also

  - <a href="/wiki/spaces/Courier/pages/2888958355/Job%2C+Courier%2C+Ad-hoc" data-linked-resource-id="2888958355" data-linked-resource-version="1" data-linked-resource-type="page">Courier Ad-hoc Job</a>

  </div>
"""

output_text_5 = """

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

def test_fix_links_5():
    assert fix_links(input_text_5) == output_text_5
