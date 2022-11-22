// 여기 db랑 연동해야함
let studentList = ["alex", "alice", "aylin", "ch", "clara", "henry", "j", "nathan", "noah", "max", "Ron", "tw"];

const LEN_OF_STUDENTS = document.getElementsByClassName("student-overoll-shortcut-inner").length;
const STUDENT_LIST_DOM = [];
for (var i = 0; i < LEN_OF_STUDENTS; i++) {
  // console.log(studentList[i]);
  STUDENT_LIST_DOM[i] = document.getElementsByClassName(studentList[i]);
}

for (var i = 0; i < LEN_OF_STUDENTS; i++) {
  console.log(i);
}
