# Package index file for tdbc::postgres

if {[catch {package require Tcl 8.6}]} {
    return
}
package ifneeded tdbc::postgres 1.0.0 \
    "[list source [file join $dir tdbcpostgres.tcl]]\;\
    [list load [file join $dir tdbcpostgres100.dll] tdbcpostgres]"
