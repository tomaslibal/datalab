function ClickManager(element, eventType, handlers) {
    function handleEvent(event) {
        var target = event.target;
        var target_classes = target.classList;

        for (var i = 0; i < target_classes.length; i += 1) {
            if (handlers[target_classes[i]]) {
                handlers[target_classes[i]](event);
            }
        }
    }
    element.addEventListener(eventType, handleEvent);
}

function q(querys, parent) {
    el = parent || document;

    return el.querySelector(querys);
}

function createElement(elType, customFactory) {
    var creator = customFactory || document;
    return creator.createElement(elType);
}

function drawAddLabelForm(parent, id) {
    var divEl = createElement('div');
    divEl.classList.add('add_label_form');
    var inputEl = createElement('input');
    inputEl.type = 'text';
    var buttonEl = createElement('button');
    buttonEl.innerHTML = 'add';
    buttonEl.addEventListener('click', function(event) {
        event.preventDefault();
        closeAddLabelHandler(divEl);
    });
    
    divEl.appendChild(inputEl);
    divEl.appendChild(buttonEl);
    parent.appendChild(divEl);
    return divEl;
}

function closeAddLabelHandler(formEl) {
    q('.add_label', formEl.parentElement).classList.remove('open_add_label');

    formEl.remove();
}

function addLabelHandler(event) {
    event.preventDefault();

    // target is the "add label" link
    var target = event.target;
   
    if (target.classList.contains('open_add_label')) {
        closeAddLabelHandler(q('.add_label_form', target.parentElement));
        return;
    }

    var id = event.target.dataset.id;

    event.target.classList.add('open_add_label');
    
    drawAddLabelForm(event.target.parentElement, id);
}

function startup(event) {
    var datapointsEl = q("#datapoints");
    var handlers = {
        "add_label": addLabelHandler
    };
    var datapointsClickMgr = new ClickManager(datapointsEl, "click", handlers);
}

document.addEventListener("DOMContentLoaded", startup);
