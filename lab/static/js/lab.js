function readCookieVal(name) {
    var cookieVal;

    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieVal = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieVal;
}

var csrfToken = readCookieVal('csrftoken');

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

function sendReq(url, method, params, callback) {
    var is_async = true;

    method = method || 'GET';

    httpRequest = new XMLHttpRequest();
    httpRequest.open(method, url, is_async);
    if (method === 'POST') {
        httpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    }
    httpRequest.setRequestHeader('X-CSRFToken', csrfToken);
    httpRequest.addEventListener('load', callback);
    httpRequest.send(params);
}

function createElement(elType, customFactory) {
    var creator = customFactory || document;
    return creator.createElement(elType);
}

function drawAddLabelForm(parent, callback) {
    var divEl = createElement('div');
    divEl.classList.add('add_label_form');
    var inputEl = createElement('input');
    inputEl.type = 'text';
    inputEl.id = 'add_label_input';
    var buttonEl = createElement('button');
    buttonEl.innerHTML = 'add';
    buttonEl.addEventListener('click', callback);
    
    divEl.appendChild(inputEl);
    divEl.appendChild(buttonEl);
    parent.appendChild(divEl);
    return divEl;
}

function closeAddLabelHandler(formEl) {
    q('.add_label', formEl.parentElement).classList.remove('open_add_label');

    formEl.remove();
}

function addDatapointHandler(event) {
    event.preventDefault();
    window.location = '/datapoint';
}

function addLabelImportHandler(event) {
    event.preventDefault();

    var target = event.target;

    if (target.classList.contains('open_add_label')) {
        closeAddLabelHandler(q('.add_label_form', target.parentElement));
        return;
    }

    event.target.classList.add('open_add_label');

    var parent = event.target.parentElement;

    function callback(event) {
        event.preventDefault();
        var inputEl = q('#add_label_input');
        var dropzoneEl = q('.dropzone');
        var inputWithLabel = createElement('input');
        inputWithLabel.type = 'hidden';
        inputWithLabel.name = 'labels[]';
        inputWithLabel.value = inputEl.value;
        dropzoneEl.appendChild(inputWithLabel);

        closeAddLabelHandler(q('.add_label_form'));

        var labelWrapEl = createElement('span');
        labelWrapEl.classList.add('mdl-chip', 'mdl-chip--deletable');
        var delBtEl = createElement('button');
        delBtEl.classList.add('mdl-chip__action');
        delBtEl.setAttribute('type', 'button');
        var iEl = createElement('i');
        iEl.classList.add('material-icons');
        iEl.innerHTML = 'cancel';
        delBtEl.appendChild(iEl);
        var labelEl = createElement('span');
        labelEl.classList.add('mdl-chip__text');
        labelEl.innerHTML = inputEl.value;
        labelWrapEl.appendChild(labelEl);
        labelWrapEl.appendChild(delBtEl);
        parent.insertBefore(labelWrapEl, parent.firstChild);
    }

    drawAddLabelForm(event.target.parentElement, callback);
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

    var parent = event.target.parentElement;

    function callback(event) {
        event.preventDefault();
        var inputEl = q('#add_label_input');
        sendReq('/api/datapoint/' + id + '/labels/', 'POST', 'name=' + inputEl.value);
        closeAddLabelHandler(q('.add_label_form'));
        var labelWrapEl = createElement('span');
        labelWrapEl.classList.add('mdl-chip', 'mdl-chip--deletable');
        var delBtEl = createElement('button');
        delBtEl.classList.add('mdl-chip__action');
        delBtEl.setAttribute('type', 'button');
        var iEl = createElement('i');
        iEl.classList.add('material-icons');
        iEl.innerHTML = 'cancel';
        delBtEl.appendChild(iEl);
        var labelEl = createElement('span');
        labelEl.classList.add('mdl-chip__text');
        labelEl.innerHTML = inputEl.value;
        labelWrapEl.appendChild(labelEl);
        labelWrapEl.appendChild(delBtEl);
        parent.insertBefore(labelWrapEl, parent.firstChild);
    }
    
    drawAddLabelForm(event.target.parentElement, callback);
}

function updateUsageNum(label_id, spanEl) {
    function onload() {
        spanEl.innerHTML = this.responseText;
    }

    sendReq('/api/labels/' + label_id + '/usagenum/', 'GET', undefined, onload);
}

function LabelsMgr(table) {
    var labels = table.querySelectorAll('.label');
    for (var i = 0; i < labels.length; i+=1) {
        var label = labels[i];
        var usagenumEl = label.querySelector('.usagenum');
        updateUsageNum(label.dataset.id, usagenumEl);
    }
}

function removeClassFromChildren(parentEl, clsName) {
    var els = parentEl.querySelectorAll('.' + clsName);
    for(var i = 0; i < els.length; i+=1) {
        els[i].classList.remove(clsName);
    }
}

function setActiveClass(el) {
    el.classList.add('active');
}

function updateActiveActionsBt(location) {
    var path = location.pathname;

    var actions = q('#actions');

    var clsName = path.replace(/\//g, '');

    removeClassFromChildren(actions, 'active');

    if (path == "/") {
        setActiveClass(q('.home', actions));
    } else {
        setActiveClass(q('.' + clsName, actions));
    }
}

function deleteDatapointHandler(event) {
    var id = event.target.dataset.id;
    var url = '/api/datapoint/' + id + '/delete';
    var datapointRow = document.querySelector("#dp" + id);
    // send a DELETE request to /api/datapoint/{{id}}
    sendReq(url, 'GET', undefined, function() {
        var res = this.responseText;
        if (res === 'OK') {
            datapointRow.remove();
        }
    });
}

function detailDatapointHandler(event){
    var id = event.target.dataset.id;
    window.location = '/datapoint/' + id;
}

function datapointLabelDeleteHandler(event) {
    var dpid = event.target.dataset.dpid;
    var label_id = event.target.dataset.id;
    function callback() {
        res = this.responseText;
        if (res === 'OK') {
            var label = q('#ll_' + dpid + '_' + label_id);
            label.remove();
        }
    }
    sendReq('/api/datapoint/' + dpid + '/label/' + label_id + '/delete', 'GET', undefined, callback);
}

function startup(event) {
    var datapointsEl = q(".datapoints_table");
    var handlersDatapointsTable = {
        "add_label": addLabelHandler,
        "dp_delete": deleteDatapointHandler,
        "dp_detail": detailDatapointHandler,
        "dp_label_delete": datapointLabelDeleteHandler
    };
    var handlersDatapointsView = {
        "add_datapoint": addDatapointHandler
    };

    var handlersDPDetail = {
        'add_label': addLabelHandler,
        "dp_label_delete": datapointLabelDeleteHandler
    };

    var handlersImportView = {
        'add_label_import': addLabelImportHandler
    };

    //updateActiveActionsBt(location);

    if (datapointsEl) {
        var datapointsClickMgr = new ClickManager(datapointsEl, "click", handlersDatapointsTable);
        var datapointsViewClickMgr = new ClickManager(document.body, "click", handlersDatapointsView);
    }

    /* labels page */
    var labelsTable = q('.labels-table');
    if (labelsTable) {
        var labelsMgr = new LabelsMgr(labelsTable);
    }

    /* datapoint details page */
    var dpDetails = q('#datapoint-details');
    if (dpDetails) {
        var clickMgr = new ClickManager(q('.mdl-cell.mdl-cell--4-col'), 'click', handlersDPDetail);
    }

    /* import page */
    var importZone = q('.import-drop-zone');
    if (importZone) {
        var clickMgr = new ClickManager(q('.click-capture-labels'), 'click', handlersImportView);
    }
}

document.addEventListener("DOMContentLoaded", startup);
