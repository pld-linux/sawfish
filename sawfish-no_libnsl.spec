diff -Nru sawfish-0.30.3/configure.in sawfish-0.30.3.new/configure.in
--- sawfish-0.30.3/configure.in	Tue Aug 22 02:00:59 2000
+++ sawfish-0.30.3.new/configure.in	Tue Aug 22 02:05:58 2000
@@ -75,7 +75,6 @@
 fi
 
 dnl Checks for libraries.
-AC_CHECK_LIB(nsl, xdr_void)
 AC_CHECK_LIB(socket, bind)
 
 dnl Checks for header files.
