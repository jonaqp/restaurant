$(function () {


    const btn_profile = $('#btn_profile');
    const frm_profile = $("#profile_form");


    $('#id_logoProfile').on('change', function () {
        const file = this.files[0];
        const type = file.type;
        const sizeInBytes = file.size;
        const sizeInMB = parseInt(Math.round((sizeInBytes / (1024 * 1024))));
        const type_reg = /^image\/(jpg|png|jpeg|bmp)$/;

        if (!(type_reg.test(type))) {
            swal('', 'This file type is unsupported.', 'error');
            $(this).parent().find('.filename').text('No file selected');
            $(this).wrap('<form>').closest('form').get(0).reset();
            return false;
        }
        if (sizeInMB > 3) {
            swal('', 'max upload size is 3MB', "error");
            $(this).parent().find('.filename').text('No file selected');
            $(this).wrap('<form>').closest('form').get(0).reset();
            return false;
        }

    });

    frm_profile.on('submit', function (e) {
        e.preventDefault();
        const id_user_uid = $("#id_user_uid").val();
        const id_document_identity = $("#id_documentIdentityTypeId").val();
        const id_documentIdentityNumber = $("#id_documentIdentityNumber").val();

        if (id_document_identity !== "") {

            if (id_documentIdentityNumber === "") {
                swal("empty field!", "enter document number", "error");
                return false;
            }
        }

        const $form = $(e.target),
            formData = new FormData(),
            params = $form.serializeArray(),
            files = $form.find(':file')[0].files;

        $.each(files, function (i, file) {
            formData.append('logoProfile', file);
        });

        $.each(params, function (i, val) {
            formData.append(val.name, val.value);
        });

        btn_profile.addClass('disabled');

        $.ajax({
            url: "/es/user-profile/" + id_user_uid + "/update/",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            type: 'POST'
        }).done(function (data) {

            if (data.status === 201) {
                func_dyn_notice("Progress", data.message, "success");
            }

            if (data.status === 301) {
                func_dyn_notice("Progress", data.message, "warning")
            }

            if (data.status === 401) {
                func_dyn_notice("Progress", data.message, "danger")
            }

        }).fail(function () {
            func_dyn_notice("Progress", "Error", "danger")
        }).always(function (data) {
            btn_profile.removeClass('disabled');
        });

        return false

    });


});
