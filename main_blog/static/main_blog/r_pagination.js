function create_li_with_logo(page_value, inner_html, disabled, aria_label) {
    var li_1 = document.createElement('li');

    var li_1_class_attr = 'page-item';

    if (disabled) {
        li_1_class_attr += ' disabled';
    }

    li_1.setAttribute('class', li_1_class_attr);

    var a_1 = document.createElement('a');
    a_1.setAttribute('class', 'page-link')
    a_1.setAttribute('href', `?page=${page_value}`);
    a_1.setAttribute('aria-label', aria_label);

    li_1.appendChild(a_1)


    var span_1 = document.createElement('span');
    span_1.setAttribute('aria-hidden', 'true');
    span_1.innerHTML = inner_html;

    a_1.appendChild(span_1);

    return li_1;

}


function create_li_for_pagination(page_value, activate = false) {
    var li_1 = document.createElement('li');
    var li_1_class_attr = 'page-item';

    if (activate) {
        li_1_class_attr += ' active';
    }
    li_1.setAttribute('class', li_1_class_attr);

    var a_1 = document.createElement('a');
    a_1.setAttribute('class', 'page-link');
    a_1.setAttribute('href', `?page=${page_value}`)
    a_1.innerHTML = `${page_value}`;
    li_1.appendChild(a_1);

    return li_1;

}

function create_li_3_dots() {
    var li_1 = document.createElement('li');
    li_1.setAttribute('class', 'page-item disabled');

    var a_1 = document.createElement('a');
    a_1.setAttribute('class', 'page-link');
    a_1.innerHTML = '...';

    li_1.appendChild(a_1);

    return li_1;
}

if (number_of_pages > 0) {

    var r1 = document.getElementById('r_pagination');


    li_previous = create_li_with_logo(current_page_start_from_1 - 1, "&laquo;", current_page_start_from_1 == 1, 'Previous');

    r1.appendChild(li_previous);


    li_1 = create_li_for_pagination(1, current_page_start_from_1 == 1);

    r1.appendChild(li_1);


    if (current_page_start_from_1 - 2 > 1) {
        li_3_dots = create_li_3_dots();

        r1.appendChild(li_3_dots);
    }

    if (current_page_start_from_1 - 1 > 1) {
        li_before_current = create_li_for_pagination(current_page_start_from_1 - 1, false);

        r1.appendChild(li_before_current);
    }

    if (current_page_start_from_1 != 1 && current_page_start_from_1 != number_of_pages) {
        li_current = create_li_for_pagination(current_page_start_from_1, true);

        r1.appendChild(li_current);
    }

    if (current_page_start_from_1 + 1 < number_of_pages) {
        li_after_current = create_li_for_pagination(current_page_start_from_1 + 1, false);

        r1.appendChild(li_after_current);
    }

    if (current_page_start_from_1 + 2 < number_of_pages) {
        li_3_dots = create_li_3_dots();

        r1.appendChild(li_3_dots);
    }


    if (number_of_pages > 1) {
        li_last = create_li_for_pagination(number_of_pages, current_page_start_from_1 == number_of_pages);

        r1.appendChild(li_last);
    }


    li_next = create_li_with_logo(current_page_start_from_1 + 1, "&raquo;", current_page_start_from_1 == number_of_pages, 'Next');

    r1.appendChild(li_next);
}





