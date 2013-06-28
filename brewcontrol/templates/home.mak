<%inherit file="base.mak"/>

<p>
    You have a few options from here:
    <ul>
        <li><a href="${request.route_url("settings")}">Set desired temperature</a></li>
        <li><a href="${request.route_url("samples")}">See the logged temperature curves</a></li>
        <li><a href="${request.route_url("shutdown")}">Turn off the heat stick</a></li> 
    </ul>
</p>
