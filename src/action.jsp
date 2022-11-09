<%@ page import = " java.util.* " %>
<%
String course_number = request.getParameter('Course-Code');
String course_name = request.getParameter('Course-Name');
String course_date = request.getParameter('Course-Day/Time');
String course_location = request.getParameter('Course-Location');
String course_semester = request.getParameter('Course-Location');

out.println(course_number);
out.println(course_name);
out.println(course_date);
out.println(course_location);
out.println(course_semester);
%>
