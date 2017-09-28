%#template for deleting a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item

<p>Edit the task with ID = {{no}}</p>
<form action="/delete/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <br>
  <input type="submit" name="save" value="save">
</form>