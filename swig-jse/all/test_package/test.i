%module PackageTest

%rename("test_regex", regextarget=1) "^XX.+";

%inline %{
extern int    gcd(int u, int v);
extern double foo;
%}
