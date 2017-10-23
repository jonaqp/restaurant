function get_FormDataSerialize(name_form) {
    const _indexed_array = name_form.serializeArray();
    const  indexed_array = {};
    $.map(_indexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}

function resetForm(form) {
    form.find('input:text, input:password, input:file, select, textarea').val('');
    form.find('input:radio, input:checkbox')
         .removeAttr('checked').removeAttr('selected');
    form.find('input[type=email]').val('');
}



// const  element = document.getElementById("foo");
function clearChildren(element) {
   for (let i = 0; i < element.childNodes.length; i++) {
      const e = element.childNodes[i];
      if (e.tagName) switch (e.tagName.toLowerCase()) {
         case 'input':
            switch (e.type) {
               case "radio":
               case "checkbox": e.checked = false; break;
               case "button":
               case "submit":
               case "image": break;
               default: e.value = ''; break;
            }
            break;
         case 'select': e.selectedIndex = 0; break;
         case 'textarea': e.innerHTML = ''; break;
         default: clearChildren(e);
      }
   }
}
