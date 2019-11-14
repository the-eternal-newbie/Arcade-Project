name "peachpy"

org 0100h
include 'emu8086.inc'


begin:                         ;Esta etiqueta es la principal y se encarga de verificar lo que se va ingresando.
    mov ah, 0                  ;Con la interrupcion 16h se introducen valores por teclado y se verifica cuaquiera
    int 16h                    ;de los casos: BACKSPACE, ENTER, signo inicial, caracter.
    
    cmp bandera_begin, 0
    je sign
    
sign:                          ;Cuando se va a ingresar el primer digito se salta a est etiqueta desde begin.
    inc bandera_begin          ;Con esta bandera validamos que al menos se ingresen dos operandos.
    mov bl, 1
    cmp al, '-'                ;Se verifica que el valor que se ingreso corresponda al ASCII del operador "-"
    jne verificar_digito       ;si no se verifica que se ingrese un digito.
    
    PUTC al
    mov signo, -1              ;si se ingreso un menos se resguarda el valor de menos uno en la variable "signo"
    mov bh, al                 ;que sera ocupada posteriormente.
    jmp begin
                               
    ADD:                       ;Si se trata de una suma simplemente se hace pop a la pila dos veces
        pop ax                 ;almacenando los valores en diferentes registros, para ser sumados y agregar
        pop bx                 ;el resultado a la pila.
        add ax, bx
        push ax
        add di, 2
        jmp resolver_loop      ;Se da un salto a "resolver_loop" para realizar el bucle.
        
    SUB:                       ;Lo que se hace en la etiqueta "sumar" es efectuado en el resto de etiquetas;
        pop bx                 ;obtener dos operandos de la pila y realizar su respectiva operacion.
        pop ax
        sub ax, bx
        push ax 
        add di, 2
        jmp resolver_loop
        
    MUL:
        pop ax
        pop bx
        mul bx
        push ax 
        add di, 2
        jmp resolver_loop
        
    DIV:
        pop bx
        pop ax
        div bx
        push ax
        add di, 2
        jmp resolver_loop            

return:         
    pop resultado          ;ultimo valor almacenado en la pila, que corresponde al resultado de la expresion
    lea si, msg_final      ;y que es guardado en un variable. Y posteriormente solo se imprime ese resultado
    call print_string      ;con la ayuda de la funcion print_num de la libreria "emu8086.inc".
    mov ax, resultado      ;El resultado tambien puede ser visualizado en su respectiva variable en el
    call print_num         ;emulador.
    
end