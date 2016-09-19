    function randomNumbers() {
        var rand1 = Math.floor((Math.random() * 100) + 1);
        var rand2 = Math.floor((Math.random() * 100) + 1);
        var rand3 = Math.floor((Math.random() * 100) + 1);
        var rand4 = Math.floor((Math.random() * 100) + 1);
        var rand5 = Math.floor((Math.random() * 100) + 1);
        var rand6 = Math.floor((Math.random() * 100) + 1);
        var rand7 = Math.floor((Math.random() * 100) + 1);
        var rand8 = Math.floor((Math.random() * 100) + 1);
        console.log(rand1, rand2, rand3, rand4, rand5, rand6, rand7, rand8);

        $("#toi1bar").css("width", rand1 + "%");
        $("#toi2bar").css("width", rand2 + "%");
        $("#toi3bar").css("width", rand3 + "%");
        $("#toi4bar").css("width", rand4 + "%");
        $("#toi5bar").css("width", rand5 + "%");
        $("#toi6bar").css("width", rand6 + "%");
        $("#toi7bar").css("width", rand7 + "%");
        $("#toi8bar").css("width", rand8 + "%");

        if (rand1 < 50) {
            $("#toi1bar").addClass('progress-bar-danger');
            $("#toi1label").text("NO");
        } else {
            $("#toi1bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi1label").text("YES");
        }

        if (rand2 < 50) {
            $("#toi2bar").addClass('progress-bar-danger');
            $("#toi2label").text("NO");
        } else {
            $("#toi2bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi2label").text("YES");
        }

        if (rand3 < 50) {
            $("#toi3bar").addClass('progress-bar-danger');
            $("#toi3label").text("NO");
        } else {
            $("#toi3bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi3label").text("YES");
        }

        if (rand4 < 50) {
            $("#toi4bar").addClass('progress-bar-danger');
            $("#toi4label").text("NO");
        } else {
            $("#toi4bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi4label").text("YES");
        }

        if (rand5 < 50) {
            $("#toi5bar").addClass('progress-bar-danger');
            $("#toi5label").text("NO");
        } else {
            $("#toi5bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi5label").text("YES");
        }

        if (rand6 < 50) {
            $("#toi6bar").addClass('progress-bar-danger');
            $("#toi6label").text("NO");
        } else {
            $("#toi6bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi6label").text("YES");
        }

        if (rand7 < 50) {
            $("#toi7bar").addClass('progress-bar-danger');
            $("#toi7label").text("NO");
        } else {
            $("#toi7bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi7label").text("YES");
        }

        if (rand8 < 50) {
            $("#toi8bar").addClass('progress-bar-danger');
            $("#toi8label").text("NO");
        } else {
            $("#toi8bar").removeClass('progress-bar-danger').addClass('progress-bar-success');
            $("#toi8label").text("YES");
        }
    };

function reloadPage() {
    location.reload();
}

$(document).ready(function () {

});
