# csjelentkezes
**Téli túrára regisztrálók adatainak mentése szerkesztés funkcióval**

*Függőségek (szerver) :*

flask flask_cors
<hr>

*Egyéb:*

Adatküldés (serverIP változó érték, definiálni kell):

```javascript
var sendingJSON = {
		"data": document.getElementById("textArea").value
}
      
$.ajax({
		type: "post",
		url: serverIP + "/bekuld",
		data: JSON.stringify(sendingJSON),
		contentType: "application/json, charset=utf-8",
		dataType:"json",
		success: function(responseData, textStatus, jqXHR) {
			alert("Sikeres változtatás");
		},
		error: function(jqXHR, textStatus, errorThrown) {
			alert("Hiba történt a szerkeztés feldolgozása közben")
		}
});
```
