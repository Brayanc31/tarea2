grammar gramatica_antlr;

s : 'a' s 'b' | 'a' 'b' ;

WS : [ \t\n\r]+ -> skip ;
