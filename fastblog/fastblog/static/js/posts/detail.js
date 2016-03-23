(function(){
  "use strict";

  $(document).ready(function(){
    $(document).ajaxStart(function(){
      $("i#comments-spinner").show();
    }).ajaxStop(function(){
      $("i#comments-spinner").hide();
    });
  });

  $(document).ready(function(){
    var comment_element = $("ul#comments");
    var post_id = comment_element.data("post-id");

    $.ajax({
      url: "/api/posts/" + post_id + "/comments/",
      type: "GET",
      success: function(comments){
        for (var i = 0; i < comments.length; i++) {
          var comment = comments[i];
          comment_element.append(
            "<li>" + comment.content + "</li>"
          );
        }
      }
    });
  });
})();
