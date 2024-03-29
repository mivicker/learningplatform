export default interface UserProgress {
  current_course: {
    title: string;
    detail_url: string;
  };
  current_lesson: {
    title: string;
    lesson_num: number;
    detail_url: string;
  };
  next_section: {
    title: string;
    section_num: number;
    detail_url: string;
  };
  announcement: string;
}
