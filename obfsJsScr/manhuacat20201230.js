var _0x486a = ['json', '&_KE=', '.pjax-container', 'chapter_num', 'parent', 'lazyload', 'decompressFromBase64', 'html', '\x22\x20href=\x22javascript:;\x22\x20onclick=\x22vg_pjax($(this));\x22\x20class=\x22btn\x20btn-primary\x20mb-1\x20pnext\x20next\x22\x20title=\x22ä¸‹ä¸€é¡µ\x22>ä¸‹é¡µ</a>\x0a\x09\x09<a\x20href=\x22javascript:goNumPage(\x27next\x27);\x22\x20class=\x22btn\x20btn-primary\x20mb-1\x20ml-1\x22\x20title=\x22ä¸‹é›†\x22>ä¸‹é›†</a>\x0a\x09\x09</div>\x0a\x09\x09</nav>\x0a\x09', 'asc', '\x22\x20title=\x22ä¸Šä¸€é¡µ\x22>ä¸Šé¡µ</a>\x0a\x09\x09<div\x20class=\x22mx-1\x20mb-1\x22>\x0a\x09\x09<label\x20for=\x22page-selector\x22\x20class=\x22sr-only\x22>ç¿»é¡µ</label>\x0a\x09\x09<select\x20class=\x22form-control\x20vg-page-selector\x22\x20id=\x22page-selector\x22\x20onchange=\x22vg_pjax($(this),\x201);\x22>\x0a\x09', 'ajax', '\x0a\x09\x09</select>\x0a\x09\x09</div>\x0a\x09\x09<a\x20data-p=\x22', '/uploads/', 'val', '/chapter_num?chapter_id=', '.pre', 'pre', 'location', 'é¡µ</option>', 'round', 'next', 'preload', '\x0a\x09\x09<nav\x20aria-label=\x22Page\x20navigation\x22>\x0a\x09\x09<div\x20class=\x22form-inline\x22>\x0a\x09\x09<a\x20href=\x22javascript:goNumPage(\x27pre\x27);\x22\x20class=\x22btn\x20btn-primary\x20mb-1\x20mr-1\x22\x20title=\x22ä¸Šé›†\x22>ä¸Šé›†</a>\x0a\x09\x09<a\x20data-p=\x22', '.sort', 'chapter-type', 'url', 'split', '&type=', 'data', 'click', 'length', 'chapter-domain', 'get', '.vg-r-data', 'fadeIn', 'keydown', 'chapter-key', 'which', 'æ²¡æœ‰å•¦ï¼ŒåŽ»å‘è¡¨ä¸‹è¯„è®ºå§', '.show-pic', 'attr', 'href', 'push', 'replace', 'selected', '?_KS=', '.html', '<option\x20value=\x22', 'src', 'code'];
(function (_0x297ff1, _0x486af2) {
    var _0x463d24 = function (_0x35d717) {
        while (--_0x35d717) {
            _0x297ff1['push'](_0x297ff1['shift']());
        }
    };
    _0x463d24(++_0x486af2);
}(_0x486a, 0x112));
var _0x463d = function (_0x297ff1, _0x486af2) {
    _0x297ff1 = _0x297ff1 - 0x0;
    var _0x463d24 = _0x486a[_0x297ff1];
    return _0x463d24;
};
var ck_num = 0x0, vg_r_data = $(_0x463d('0xf'));
let img_data_arr = LZString[_0x463d('0x26')](img_data)[_0x463d('0x8')](','), total_page = img_data_arr['length'];
var asset_domain = vg_r_data[_0x463d('0xa')](_0x463d('0xd')), asset_key = vg_r_data[_0x463d('0xa')](_0x463d('0x12')),
    img_pre = _0x463d('0x2d'), chapter_num = vg_r_data[_0x463d('0xa')](_0x463d('0x23')),
    chapter_type = vg_r_data[_0x463d('0xa')](_0x463d('0x6'));
$(function () {
    vg_pagination(page, total_page), $(_0x463d('0x15'))[_0x463d('0x16')](_0x463d('0x1e'), cdnImage(img_pre + img_data_arr[parseInt(page) - 0x1], asset_domain, asset_key)), preload(), $('.relation-cc\x20img')[_0x463d('0x25')]({'effect': _0x463d('0x10')});
    page > 0x1 && scroll_top();
    var _0x6a956b = $(_0x463d('0x5')), _0x46d74e = 0x0;
    _0x6a956b[_0x463d('0xb')](
        function () {
        var _0x26062c = $(this)[_0x463d('0x24')]()[_0x463d('0x24')]()[_0x463d('0x24')]()['find']('.num_div');
        _0x46d74e == 0x0 ? (sortNum(_0x26062c, 'desc'), _0x46d74e = 0x1) : (sortNum(_0x26062c, _0x463d('0x29')), _0x46d74e = 0x0);
    }), $(document)[_0x463d('0x11')](function (_0x462999) {
        if (_0x462999[_0x463d('0x13')] == 0x25) vg_pjax($(_0x463d('0x30'))[_0x463d('0xa')]('p'), 0x2);
        if (_0x462999[_0x463d('0x13')] == 0x27) vg_pjax($('.next')[_0x463d('0xa')]('p'), 0x2);
    });
});

function cdnImage(_0x3a5c91, _0x88a819, _0x160496) {
    return time_exp = Math[_0x463d('0x1')](new Date() / 0x3e8), ks_md5_path = _0x3a5c91 + _0x160496 + time_exp, ks_md5 = $['md5'](ks_md5_path), _0x88a819 + _0x3a5c91 + _0x463d('0x1b') + ks_md5 + _0x463d('0x21') + time_exp;
}

var preload = () => {
    var _0x3cffb0 = [], _0x4fb9f4 = parseInt(page);
    for (let _0x372878 in img_data_arr) {
        (_0x372878 == _0x4fb9f4 || _0x372878 == _0x4fb9f4 + 0x1) && _0x3cffb0[_0x463d('0x18')](cdnImage(img_pre + img_data_arr[_0x372878], asset_domain, asset_key));
    }
    _0x3cffb0[_0x463d('0xc')] > 0x0 && $[_0x463d('0x3')](_0x3cffb0);
}
var vg_pagination = (_0x31d1ad, _0x179222) => {
    let _0x2b7b79 = parseInt(_0x31d1ad) - 0x1, _0x4b534c = parseInt(_0x31d1ad) + 0x1,
        _0x165aed = !_0x2b7b79 ? 'disabled' : '';
    _0x2b7b79 <= 0x1 && (_0x2b7b79 = 0x1);
    let _0xfffe1f = _0x463d('0x4') + _0x2b7b79 + '\x22\x20href=\x22javascript:;\x22\x20onclick=\x22vg_pjax($(this));\x22\x20class=\x22btn\x20btn-primary\x20mb-1\x20ppre\x20pre\x20' + _0x165aed + _0x463d('0x2a');
    for (var _0x121768 = 0x1; _0x121768 <= _0x179222; _0x121768++) {
        let _0x13f747 = _0x121768 == _0x31d1ad ? _0x463d('0x1a') : '';
        _0xfffe1f += _0x463d('0x1d') + _0x121768 + '\x22\x20' + _0x13f747 + '>ç¬¬' + _0x121768 + _0x463d('0x0');
    }
    _0xfffe1f += _0x463d('0x2c') + _0x4b534c + _0x463d('0x28'), $('.pagination')[_0x463d('0x27')](_0xfffe1f);
};

function goNumPage(_0x38b14a) {
    let _0x2d6c0b;
    if (_0x38b14a == 'pre') _0x2d6c0b = 0x2; else _0x38b14a == _0x463d('0x2') && (_0x2d6c0b = 0x1);
    $[_0x463d('0x2b')]({
        'type': _0x463d('0xe'),
        'url': _0x463d('0x2f') + chapter_num + '&ctype=' + _0x2d6c0b + _0x463d('0x9') + chapter_type,
        'dataType': _0x463d('0x20'),
        'success': function (_0x20492e) {
            if (_0x20492e[_0x463d('0x1f')] != '0000') alert(_0x463d('0x14')); else {
                let _0x28ab63 = _0x20492e[_0x463d('0x7')];
                window[_0x463d('0x32')][_0x463d('0x17')] = _0x28ab63;
            }
        }
    });
}
// _0x5404b9 = .pjax-container
var vg_pjax = (_0x2047df, _0x5df2c6 = 0x0, _0x5404b9 = _0x463d('0x22')) => {
    let _0x1f31db = _0x5404b9, _0xd8a275;
    scroll_top();
    if (_0x5df2c6 == 0x1) _0xd8a275 = parseInt(_0x2047df[_0x463d('0x2e')]()); else _0x5df2c6 == 0x2 ? _0xd8a275 = _0x2047df : _0xd8a275 = parseInt(_0x2047df['data']('p'));
    var _0x8bc8fd = new Image();
    $('.loading')['show']();
    var _0x51d1da = _0xd8a275 - 0x1,
        _0x59383b = img_data_arr[_0x51d1da] ? cdnImage(img_pre + img_data_arr[_0x51d1da], asset_domain, asset_key) : '';
    if (_0xd8a275 <= 0x0) {
        goNumPage(_0x463d('0x31'));
        return;
    } else {
        if (_0xd8a275 > total_page) {
            alert('æœ¬ç« å·²å®Œï¼Œå‰å¾€ä¸‹ä¸€ç« ï¼'), goNumPage(_0x463d('0x2'));
            return;
        }
    }
    let _0x116600 = cur_url;
    _0x116600 = _0x116600[_0x463d('0x19')]('.html', '_' + _0xd8a275 + _0x463d('0x1c')), window['location'][_0x463d('0x17')] = _0x116600;
};