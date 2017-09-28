%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<table border="4">
<caption> <b> Advance Database Class Table </b> </caption>
<br>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
<br>

<form action="/do_insert" method="GET">
<table border = "4">
<tr>
  <td> click to insert the data </td>
  <td> 
  <input type="submit" name="Insert" value="Insert" /> </td> 
  </td>
</tr>
</table>
</form>

<form action="/find_edit" method="GET">
<table border="4">
<tr>
<td> Edit ID </td>
  <td>
<input type="text" name ='editdata' />
  </td> 
  <td> <input type="submit" name="Edit" value="Edit" /> </td>
</tr>
</table>
</form>


<form action="/find_delete" method="GET">
<table border="4">
<tr>
<td>Delete ID </td>
   <td>
   <input type="text" name ='deletedata' />
   </td> 
   <td> <input type="submit" name="Delete" value="Delete" /> </td>

</tr>
</table>
</form>

