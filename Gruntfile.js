module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      options: {
        includePaths: ['app/sass']
      },
      dist: {
        files: {
          'app/static/css/style.css': 'sass/style.scss'
        }
      }
    },
    watch: {
      sass: {
        files: 'app/sass/*.scss',
        tasks: 'sass'
      }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default', ['sass']);
};
