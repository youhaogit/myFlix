
    var QS_PAGE_PREFIX = "?page="

    // bottom navigation init
    $(function () {

        var DEFAULT_MID_VALUE = sessionStorage.getItem('DEFAULT_MID_VALUE');
        console.log('init mid value ' + DEFAULT_MID_VALUE);

        if(DEFAULT_MID_VALUE == null) {
            sessionStorage.setItem('DEFAULT_MID_VALUE', 1);
            $('#page_left').hide()
        }
        if(DEFAULT_MID_VALUE == 1) {
               $('#page_left').hide()
        }

        DEFAULT_MID_VALUE = parseInt(sessionStorage.getItem('DEFAULT_MID_VALUE'));

        $('#page_left').text(DEFAULT_MID_VALUE - 1);
        $('#page_mid').text(DEFAULT_MID_VALUE);
        $('#page_right').text(DEFAULT_MID_VALUE + 1);

    })

    // change btm nav text accordingly
    $(".pagination").each(function () {
        var context = $(this),
            page_left = context.find('#page_left'),
            page_mid = context.find('#page_mid'),
            page_right = context.find('#page_right'),
            page_pre = context.find('#page_pre'),
            page_next = context.find('#page_next');



        $(page_right).click(function(){
            var RIGHT_VAL = parseInt($(this).text());
            console.log('page right clicked');
            console.log(RIGHT_VAL);

            MID_VAL = RIGHT_VAL;
            $(page_left).text(MID_VAL - 1);
            $(page_mid).text(MID_VAL);
            $(page_right).text(MID_VAL + 1);

            sessionStorage.setItem('DEFAULT_MID_VALUE', MID_VAL);

            $(this).prop('href', QS_PAGE_PREFIX + (MID_VAL))

        });

        $(page_left).click(function(){
            var LEFT_VAL = parseInt($(this).text());

            MID_VAL = LEFT_VAL;
            $(page_left).text(MID_VAL - 1);
            $(page_mid).text(MID_VAL);
            $(page_right).text(MID_VAL + 1);

            sessionStorage.setItem('DEFAULT_MID_VALUE', MID_VAL);

            $(this).prop('href', QS_PAGE_PREFIX + (MID_VAL))
        });

        $(page_pre).click(function(){
            var MID_VAL = parseInt($(page_mid).text());

            console.log('here');
            console.log(MID_VAL);

            if (MID_VAL == 1) {
                return false;
            };

            MID_VAL = MID_VAL - 1;
            sessionStorage.setItem('DEFAULT_MID_VALUE', MID_VAL);

            if(MID_VAL == 1) {
               $('#page_left').hide()
            }else {
                $(page_left).text(MID_VAL - 1);
            }

            $(page_mid).text(MID_VAL);
            $(page_right).text(MID_VAL + 1);

            $(this).prop('href', QS_PAGE_PREFIX + (MID_VAL))

        });

        $(page_next).click(function(){
            var MID_VAL = parseInt($(page_mid).text());

            MID_VAL = MID_VAL + 1;
            $(page_left).text(MID_VAL - 1);
            $(page_mid).text(MID_VAL);
            $(page_right).text(MID_VAL + 1);

            sessionStorage.setItem('DEFAULT_MID_VALUE', MID_VAL);

            $(this).prop('href', QS_PAGE_PREFIX + (MID_VAL))

        });


    });




