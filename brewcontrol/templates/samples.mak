<%inherit file="base.mak"/>

<%!

    from brewcontrol.sensors import path_to_id

%>

<p>
  Those are the last few logged samples <br>

  <table>
    <tr>
        <td>date</td>
        <td>sensor</td>
        <td>temp</td>
    </tr>

    % for sample in samples:
      % if True:
          <tr>
            <td>${sample.date.isoformat()}</td>
            <td>${path_to_id(sample.sensor)}</td>
            <td>${sample.temp / 1000.0}</td>
          </tr>
      % endif
    % endfor

  </table>
</p>
