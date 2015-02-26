var gulp = require('gulp');
var uncss = require('gulp-uncss');

gulp.task('default', function() {
    return gulp.src('static/css/**/*.css')
        .pipe(uncss({
              html: [
                'https://tarjimonlar.org',
                'https://tarjimonlar.org/members',
                'https://tarjimonlar.org/posts',
                'https://tarjimonlar.org/comments',
                'https://tarjimonlar.org/search',
                'https://tarjimonlar.org/search?q=tashkent',
                'https://tarjimonlar.org/about'
                ]
        }))
        .pipe(gulp.dest('./out.css'));
});
