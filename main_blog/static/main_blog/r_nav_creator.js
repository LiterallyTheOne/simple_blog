function create_li_for_nav(target_id, target_content, margins) {
    li_1 = document.createElement('li');

    var li_1_class_attr = 'nav-item';

    for (var m1 in margins) {
        li_1_class_attr += ` ${margins[m1]}`;
    }

    li_1.setAttribute('class', li_1_class_attr);

    a_1 = document.createElement('a');
    a_1.setAttribute('class', 'nav-link');
    a_1.setAttribute('href', `#${target_id}`);
    a_1.innerHTML = target_content;

    li_1.appendChild(a_1);

    return li_1;

}

function create_ul_for_nested_elements() {
    ul_1 = document.createElement('ul');
    ul_1.setAttribute('class', 'nav nav-pills list-group');
    return ul_1;
}

var r1 = document.getElementById('r-nav-ul');

var post_description = document.getElementById('post-description');


var hs = post_description.querySelectorAll("h2, h3, h4, h5, h6");

if (hs.length > 0) {
    var current = 0;
    var current_h = hs[0].tagName.slice(1);

    var add_to = [r1];

    var perv_k1 = null;

    for (var i = 0; i < hs.length; i++) {

        if (current_h < hs[i].tagName.slice(1)) {
            current++;
            var target_ul = create_ul_for_nested_elements();
            perv_k1.appendChild(target_ul);
            add_to.push(target_ul);

        } else if (current_h > hs[i].tagName.slice(1)) {
            current -= parseInt(current_h) - parseInt(hs[i].tagName.slice(1));
            for (var j = 0; j < (parseInt(current_h) - parseInt(hs[i].tagName.slice(1))); j++) {
                add_to.pop();
            }

        }
        current_h = hs[i].tagName.slice(1);

        hs_id = hs[i].getAttribute('id')
        if (hs_id == null) {
            hs_id = hs[i].parentNode.id;
        }

        var k1 = create_li_for_nav(hs_id, hs[i].innerHTML, ['my-1', `ms-${current + 2}`]);

        perv_k1 = k1;

        add_to[current].appendChild(k1);
    }
}

