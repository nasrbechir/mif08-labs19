//define a tiny grammar for arith expressions with identifiers

grammar Example2;

r: expr ';' ;

expr: expr OP expr
    | ID {print('oh an id : '+$ID.text);}
    | INT 
    ;

OP : '+'| '*' | '-' | '/' ;


INT :   '0'..'9'+ ;
ID :   ('a'..'z'|'A'..'Z')+ ;
WS : [ \t\r\n]+ -> skip ;          // skip spaces, tabs, newlines
