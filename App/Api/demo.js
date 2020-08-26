<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>W3Cschool教程 React 实例</title>
    <script src="//www.w3cschool.cn/statics/assets/react/react.min.js"></script>
    <script src="//www.w3cschool.cn/statics/assets/react/react-dom.min.js"></script>
    <script src="//www.w3cschool.cn/statics/assets/react/babel.min.js"></script>
  </head>
  <body>
    <div id="example"></div>
    <script type="text/babel">
      ReactDOM.render(
      	<div>
      	<h1>W3Cschool教程</h1>
      	<h2>欢迎学习 React</h2>
        <p data-myattribute = "somevalue">这是一个很不错的 JavaScript 库!</p>
        </div>
      	,
      	document.getElementById('example')
      );
    </script>
  </body>
</html>