<html>
<body>
<h2>Shopping List - Sqlite3 Using Dataset Library</h2>
<hr/>
<table>
</tr>
 <th> Item </th>
 <th> Quantity </th>
 <th> </th>
 <th> </th>
<tr>

% for item in shopping_list:
  <tr>
    <td>{{str(item['description'])}}</td>
    <td>{{str(item['quantity'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/add" method="post">
  <p>New item: <input name="description"/></p>
  <p>Quantity: <input name="quantity"/></p>
  <p><button type="submit">Add Item</button>
</form>
</body>
</html>
