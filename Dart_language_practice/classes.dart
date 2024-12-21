class Person
{
  String firstname;

  Person(this.firstname);

  print_name()
  {
    print(this.firstname);
  }
}

void main()
{
  var person = new Person('Janmay');
  person.print_name();
}