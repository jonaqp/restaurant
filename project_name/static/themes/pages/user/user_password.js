$(function () {

    const btn_user = $('#btn_user');
    const frm_user = $("#user_form");


    btn_user.on('click', function (e) {
        e.preventDefault();

        const id_user_uid = $("#id_user_uid").val();

        const id_current_password = $("#id_current_password").val();
        const id_password1 = $("#id_password1").val();
        const id_password2 = $("#id_password2").val();

        if (id_current_password === "") {
            swal("empty field!", "current password", "error");
            return false;
        }
        if (id_password1 === "") {
            swal("empty field!", "new password", "error");
            return false;
        }
        if (id_password2 === "") {
            swal("empty field!", "repeat password", "error");
            return false;
        }

        if (id_password1 !== id_password2) {
            swal("field!", "passwords don't match", "error");
            return false;
        }

        const parameter = get_FormDataSerialize($("#user_form"));
        btn_user.addClass('disabled');

        $.post("/es/user-password/" + id_user_uid + "/update/", parameter, function (data) {
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
            btn_user.removeClass('disabled');

        });
    });
    return false

});

