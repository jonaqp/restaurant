const X = XLSX;
const XW = {
    msg: 'xlsx',
    rABS: xlsxworker2,
    norABS: xlsxworker1,
    noxfer: xlsxworker
};

const rABS = typeof FileReader !== "undefined" && typeof FileReader.prototype !== "undefined" && typeof FileReader.prototype.readAsBinaryString !== "undefined";


function ab2str(data) {
    let o = "", l = 0, w = 10240;
    for (; l < data.byteLength / w; ++l) o += String.fromCharCode.apply(null, new Uint16Array(data.slice(l * w, l * w + w)));
    o += String.fromCharCode.apply(null, new Uint16Array(data.slice(l * w)));
    return o;
}

function s2ab(s) {
    let b = new ArrayBuffer(s.length * 2), v = new Uint16Array(b);
    for (let i = 0; i != s.length; ++i) v[i] = s.charCodeAt(i);
    return [v, b];
}

function xw_xfer(data, cb) {
    const worker = new Worker(rABS ? XW.rABS : XW.norABS);
    worker.onmessage = function (e) {
        switch (e.data.t) {
            case 'ready':
                break;
            case 'e':
                console.error(e.data.d);
                break;
            default:
                let xx = ab2str(e.data).replace(/\n/g, "\\n").replace(/\r/g, "\\r");
                console.log("done");
                cb(JSON.parse(xx));
                break;
        }
    };
    if (rABS) {
        const val = s2ab(data);
        worker.postMessage(val[1], [val[1]]);
    } else {
        worker.postMessage(data, [data]);
    }
}

function xw(data, cb) {
    xw_xfer(data, cb);
}


function to_json(workbook) {
    var result = {};
    var json_array = [];

    workbook.SheetNames.forEach(function (sheetName) {
        var roa = X.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
        for (var a in roa) {
            var map = roa[a];
            var data_array = [];
            Object.keys(map).forEach(function (key) {
                value = map[key];
                data_array.push(map[key])
            });
            json_array.push(data_array)
        }


    });
    return json_array;
}


function process_wb(wb) {
    let output = JSON.stringify(to_json(wb), 2, 2);
    if (out2.innerText === undefined) out2.textContent = output;
    else out2.innerText = output;
    if (typeof console !== 'undefined') console.log("output", new Date());
}



