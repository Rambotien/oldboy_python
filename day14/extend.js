/**
 * Created by alex on 2016/4/23.
 */

(function(arg){
    arg.extend({
      qinghua: function() {
        return "SB";
      },
      qinghua1: function() {
        return this.each(function() { this.checked = false; });
      }
    });

    arg.fn.extend({
       sanjiang:function(){
           return "DSB"
       }
    });
})(jQuery);

