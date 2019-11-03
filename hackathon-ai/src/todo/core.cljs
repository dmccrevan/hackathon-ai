(ns todo.core)

; Find the elements and bind to names
(def form  (.getElementById js/document "todo-form"))
(def input (.getElementById js/document "todo-inp" ))
(def list-elm  (.getElementById js/document "todo-list"))
; clone it to keep in memory in case it is removed
(def hidden-item (.cloneNode (.querySelector list-elm ".todo-item") true))

(def localstorage (.-localStorage js/window))


; Get the list from localstorage and do type conversions
(defn get-list []
    (js->clj
        (.parse js/JSON (.getItem localstorage "todolist"))
        :keywordize-keys true))

; Set the todolist to either the stored list or an empty vector
(def todolist (let [newlist (get-list)] (if (nil? newlist) [] newlist)))

; Pre-declaration
(declare create-item)

; Set the new list into localstorage after type conversions
(defn set-list [newlist]
    (set! todolist newlist)
    (set! (.-innerHTML list-elm) "")
    (doseq [entry newlist] (create-item entry))
    (.setItem localstorage "todolist" (.stringify js/JSON (clj->js newlist))))

; Add event listeners
(set! (.-onsubmit form)
    (fn [event]
        (.preventDefault event)
        (let [newlist (conj todolist { :task (.-value input) :done false } )]
            (set-list newlist))
        (set! (.-value input) "")))

; Create a list item and add it to the list
(defn create-item [entry]
    (let [cloned (.cloneNode hidden-item true)]
        (set! (.-display (.-style cloned)) "initial")
        (set! (.-innerHTML (.querySelector cloned ".todo-text")) (:task entry))
        (if (:done entry) (set! (.-textDecoration (.-style cloned)) "line-through"))
        (set! (.-onclick (.querySelector cloned ".todo-toggle"))
            (fn [event]
                (.preventDefault event)
                (set-list
                    (assoc todolist
                        (.indexOf todolist entry)
                        { :task (:task entry) :done (not (:done entry)) }))
            ))
        (.appendChild list-elm cloned)
    ))

(set! (.-onclick (.querySelector js/document "#todo-clear"))
    (fn [] (set-list (into [] (filter (fn [e] (not (:done e))) todolist)))))

; setup the initial todo items
(doseq [entry todolist] (create-item entry))
