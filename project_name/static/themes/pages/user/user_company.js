$(function () {

    $.extend($.fn.dataTable.defaults, {
        autoWidth: false,
        responsive: true,
        dom: '<"datatable-header"fl><"datatable-scroll-wrap"t><"datatable-footer"ip>',
        language: {
            search: '<span>Filter:</span> _INPUT_',
            lengthMenu: '_MENU_',
            paginate: {'first': 'First', 'last': 'Last', 'next': '&rarr;', 'previous': '&larr;'}
        }
    });

    $.extend($.fn.dataTableExt.oStdClasses, {
        "sFilterInput": "form-control",
        "sLengthSelect": "form-control"
    });

    const id_tbody_company_list = $('#id_tbody_company_list');
    const btn_add_company = $('#btn_add_company');
    const id_reload_table = $('#id_reload_table');
    const tbl_company_list = $('#tbl_company_list');

    tbl_company_list.DataTable();


    btn_add_company.on('click', function () {
        const id_type_document = $("input[name=document_type]:checked");
        const id_doc_number = $("#id_document_number").val();
        const id_country = $("#id_country").val();
        const id_trade_name = $("#id_trade_name").val();
        const id_trade_name_alias = $("#id_trade_name_alias").val();

        if (id_type_document.length <= 0){
             swal("empty field!","enter type document", "error");
            return false;
        }

        if (id_doc_number === "") {
            swal("empty field!","enter document number", "error");
            return false;
        }
        if (id_country === "") {
             swal("empty field!","choice country", "error");
            return false;
        }
        if (id_trade_name === "") {
            swal("empty field!","enter trade name", "error");
            return false;
        }
        if (id_trade_name_alias === "") {
            swal("empty field!","enter trade name alias", "error");
            return false;
        }

        const paramenter = get_FormDataSerialize($("#company_form"));
        btn_add_company.addClass('disabled');
        $.post("/es/user-company/add/", paramenter, function (data) {
        })
            .done(function (data) {
                if (data.status === 201) {
                    func_dyn_notice("Progress", data.message, "success");
                    setTimeout(function () {
                        id_reload_table.trigger('click');
                    }, 2000);
                }
                if (data.status === 301) {
                    func_dyn_notice("Progress", data.message, "warning")
                }
                if (data.status === 401) {
                    func_dyn_notice("Progress", data.message, "danger")
                }


            })
            .fail(function () {
                func_dyn_notice("Progreso", "Error", "danger")
            })
            .always(function (data) {
                btn_add_company.removeClass('disabled');
            });


    });

    id_reload_table.on('click', function () {
        $.get("/es/user-company/list/", function (data) {
        })
            .done(function (data) {
                if (data !== null) {
                    func_reload_table(id_reload_table);
                    tbl_company_list.DataTable().destroy();
                    id_tbody_company_list.empty();
                    $.each(data.results, function (key, value) {
                        const counter = key + 1;
                        let html_tbody_article = `
                        <tr class='tr_${value.id}'>
                            <td><b>${counter}.-</b></td>
                            <td>${value.country}</td>
                            <td>${value.document_type}</td>
                            <td>${value.document_number}</td>
                            <td>${value.trade_name}</td>
                            <td>${value.trade_name_alias}</td>
                        </tr>`;
                        id_tbody_company_list.append(html_tbody_article)
                    });
                    tbl_company_list.DataTable();
                    $('.blockOverlay').trigger('click');
                }
            })
    });

});
