function redirect_js(url) {
    let ua = navigator.userAgent.toLowerCase(),
        isIE = ua.indexOf('msie') !== -1,
        version = parseInt(ua.substr(4, 2), 10);

    // Internet Explorer 8 and lower
    if (isIE && version < 9) {
        let link = document.createElement('a');
        link.href = url;
        document.body.appendChild(link);
        link.click();
    }

    // All other browsers can use the standard window.location.href (they don't lose HTTP_REFERER like Internet Explorer 8 & lower does)
    else {
        window.location.href = url;
    }
}


function func_reload_table(_this) {
    const block = _this.parent().parent().parent().parent().parent();

    $(block).block({
        message: '<span class="text-semibold"><i class="icon-spinner4 spinner position-left"></i>&nbsp; Updating data</span>',
        overlayCSS: {
            backgroundColor: '#fff',
            opacity: 0.8,
            cursor: 'wait'
        },
        css: {
            border: 0,
            padding: '10px 15px',
            color: '#fff',
            width: 'auto',
            '-webkit-border-radius': 2,
            '-moz-border-radius': 2,
            backgroundColor: '#333'
        }
    });


    $('.blockOverlay').on('click', function () {
        setTimeout(function () {
            $(block).unblock();
        }, 2000);
    });
}

function func_dyn_notice(title80, message, type_result) {
    let percent = 0;
    const notice = new PNotify({
        text: "Please Wait",
        addclass: 'bg-primary',
        type: 'info',
        icon: 'icon-spinner4 spinner',
        hide: false,
        buttons: {
            closer: false,
            sticker: false
        },
        shadow: false,
        width: "170px"
    });

    setTimeout(function () {
        notice.update({title: false});
        const interval = setInterval(function () {
            percent += 10;
            const options = {
                text: percent + "% complete."
            };
            if (percent < 80)
                options.title = title80;
            options.addclass = 'bg-info';

            if (percent === 80)
                options.title = title80;
            if (percent >= 100) {
                window.clearInterval(interval);
                options.title = message;

                if (type_result === 'success') {
                    options.addclass = 'bg-success';
                    options.type = "success";
                    options.icon = 'icon-checkmark3';
                }
                if (type_result === 'warning') {
                    options.addclass = 'bg-warning';
                    options.type = "warning";
                    options.icon = 'icon-info22';
                }
                if (type_result === 'danger') {
                    options.addclass = 'bg-danger';
                    options.type = "error";
                    options.icon = 'icon-blocked';

                }

                options.hide = true;
                options.buttons = {
                    closer: true,
                    sticker: true
                };
                options.shadow = true;
                options.width = PNotify.prototype.options.width;
            }
            notice.update(options);
        }, 100);
    }, 2000);
}

function isEmail(email) {
  const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}



$(document).ready(function () {
    "use strict";

    /** ONLY NUMEROS **/
    $(".is-numeric").keydown(function (e) {
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
            (e.keyCode == 65 && e.ctrlKey === true) ||
            (e.keyCode >= 35 && e.keyCode <= 39)) {
            return;
        }
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });

});
