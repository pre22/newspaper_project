Creating our custom user model requires four steps:

1. Update settings.py
2. create a new CustomeUser model
3. Create a new forms for UserCreationForm and UserChangeForm
4. Update users/admin.py

A common gotcha to be aware of is that the field type dictates how to use these values.
Whenever you have a string-based field like CharField or TextField, setting both null
and blank as we’ve done will result in two possible values for “no data” in the database.
Which is a bad idea. The Django convention is instead to use the empty string '', not
NULL.

