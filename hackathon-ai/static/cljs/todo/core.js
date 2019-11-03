// Compiled by ClojureScript 1.10.520 {:static-fns true, :optimize-constants true}
goog.provide('todo.core');
goog.require('cljs.core');
goog.require('cljs.core.constants');
todo.core.form = document.getElementById("todo-form");
todo.core.input = document.getElementById("todo-inp");
todo.core.list_elm = document.getElementById("todo-list");
todo.core.hidden_item = todo.core.list_elm.querySelector(".todo-item").cloneNode(true);
todo.core.localstorage = window.localStorage;
todo.core.get_list = (function todo$core$get_list(){
return cljs.core.js__GT_clj.cljs$core$IFn$_invoke$arity$variadic(JSON.parse(todo.core.localstorage.getItem("todolist")),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([cljs.core.cst$kw$keywordize_DASH_keys,true], 0));
});
todo.core.todolist = (function (){var newlist = todo.core.get_list();
if((newlist == null)){
return cljs.core.PersistentVector.EMPTY;
} else {
return newlist;
}
})();
todo.core.set_list = (function todo$core$set_list(newlist){
todo.core.todolist = newlist;

todo.core.list_elm.innerHTML = "";

var seq__526_530 = cljs.core.seq(newlist);
var chunk__527_531 = null;
var count__528_532 = (0);
var i__529_533 = (0);
while(true){
if((i__529_533 < count__528_532)){
var entry_534 = chunk__527_531.cljs$core$IIndexed$_nth$arity$2(null,i__529_533);
(todo.core.create_item.cljs$core$IFn$_invoke$arity$1 ? todo.core.create_item.cljs$core$IFn$_invoke$arity$1(entry_534) : todo.core.create_item.call(null,entry_534));


var G__535 = seq__526_530;
var G__536 = chunk__527_531;
var G__537 = count__528_532;
var G__538 = (i__529_533 + (1));
seq__526_530 = G__535;
chunk__527_531 = G__536;
count__528_532 = G__537;
i__529_533 = G__538;
continue;
} else {
var temp__5735__auto___539 = cljs.core.seq(seq__526_530);
if(temp__5735__auto___539){
var seq__526_540__$1 = temp__5735__auto___539;
if(cljs.core.chunked_seq_QMARK_(seq__526_540__$1)){
var c__4550__auto___541 = cljs.core.chunk_first(seq__526_540__$1);
var G__542 = cljs.core.chunk_rest(seq__526_540__$1);
var G__543 = c__4550__auto___541;
var G__544 = cljs.core.count(c__4550__auto___541);
var G__545 = (0);
seq__526_530 = G__542;
chunk__527_531 = G__543;
count__528_532 = G__544;
i__529_533 = G__545;
continue;
} else {
var entry_546 = cljs.core.first(seq__526_540__$1);
(todo.core.create_item.cljs$core$IFn$_invoke$arity$1 ? todo.core.create_item.cljs$core$IFn$_invoke$arity$1(entry_546) : todo.core.create_item.call(null,entry_546));


var G__547 = cljs.core.next(seq__526_540__$1);
var G__548 = null;
var G__549 = (0);
var G__550 = (0);
seq__526_530 = G__547;
chunk__527_531 = G__548;
count__528_532 = G__549;
i__529_533 = G__550;
continue;
}
} else {
}
}
break;
}

return todo.core.localstorage.setItem("todolist",JSON.stringify(cljs.core.clj__GT_js(newlist)));
});
todo.core.form.onsubmit = (function (event){
event.preventDefault();

var newlist_551 = cljs.core.conj.cljs$core$IFn$_invoke$arity$2(todo.core.todolist,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$task,todo.core.input.value,cljs.core.cst$kw$done,false], null));
todo.core.set_list(newlist_551);

return todo.core.input.value = "";
});
todo.core.create_item = (function todo$core$create_item(entry){
var cloned = todo.core.hidden_item.cloneNode(true);
cloned.style.display = "initial";

cloned.querySelector(".todo-text").innerHTML = cljs.core.cst$kw$task.cljs$core$IFn$_invoke$arity$1(entry);

if(cljs.core.truth_(cljs.core.cst$kw$done.cljs$core$IFn$_invoke$arity$1(entry))){
cloned.style.textDecoration = "line-through";
} else {
}

cloned.querySelector(".todo-toggle").onclick = ((function (cloned){
return (function (event){
event.preventDefault();

return todo.core.set_list(cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(todo.core.todolist,todo.core.todolist.indexOf(entry),new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$task,cljs.core.cst$kw$task.cljs$core$IFn$_invoke$arity$1(entry),cljs.core.cst$kw$done,cljs.core.not(cljs.core.cst$kw$done.cljs$core$IFn$_invoke$arity$1(entry))], null)));
});})(cloned))
;

return todo.core.list_elm.appendChild(cloned);
});
document.querySelector("#todo-clear").onclick = (function (){
return todo.core.set_list(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentVector.EMPTY,cljs.core.filter.cljs$core$IFn$_invoke$arity$2((function (e){
return cljs.core.not(cljs.core.cst$kw$done.cljs$core$IFn$_invoke$arity$1(e));
}),todo.core.todolist)));
});
var seq__552_556 = cljs.core.seq(todo.core.todolist);
var chunk__553_557 = null;
var count__554_558 = (0);
var i__555_559 = (0);
while(true){
if((i__555_559 < count__554_558)){
var entry_560 = chunk__553_557.cljs$core$IIndexed$_nth$arity$2(null,i__555_559);
todo.core.create_item(entry_560);


var G__561 = seq__552_556;
var G__562 = chunk__553_557;
var G__563 = count__554_558;
var G__564 = (i__555_559 + (1));
seq__552_556 = G__561;
chunk__553_557 = G__562;
count__554_558 = G__563;
i__555_559 = G__564;
continue;
} else {
var temp__5735__auto___565 = cljs.core.seq(seq__552_556);
if(temp__5735__auto___565){
var seq__552_566__$1 = temp__5735__auto___565;
if(cljs.core.chunked_seq_QMARK_(seq__552_566__$1)){
var c__4550__auto___567 = cljs.core.chunk_first(seq__552_566__$1);
var G__568 = cljs.core.chunk_rest(seq__552_566__$1);
var G__569 = c__4550__auto___567;
var G__570 = cljs.core.count(c__4550__auto___567);
var G__571 = (0);
seq__552_556 = G__568;
chunk__553_557 = G__569;
count__554_558 = G__570;
i__555_559 = G__571;
continue;
} else {
var entry_572 = cljs.core.first(seq__552_566__$1);
todo.core.create_item(entry_572);


var G__573 = cljs.core.next(seq__552_566__$1);
var G__574 = null;
var G__575 = (0);
var G__576 = (0);
seq__552_556 = G__573;
chunk__553_557 = G__574;
count__554_558 = G__575;
i__555_559 = G__576;
continue;
}
} else {
}
}
break;
}
