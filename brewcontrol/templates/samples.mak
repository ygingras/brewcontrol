<%inherit file="base.mak"/>

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
            <td>${sample.sensor[len('/sys/bus/w1/devices/'):].split()[0]}</td>
            <td>${sample.temp / 1000.0}</td>
          </tr>
      % endif
    % endfor

  </table>
</p>
