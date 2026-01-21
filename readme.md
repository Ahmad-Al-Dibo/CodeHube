# Tracking for Every New Functionality & Feature

<details open>
<summary><strong>📌 Overzicht & Werkwijze</strong></summary>

To keep track of every new functionality and feature added to the **CursesPlatform** project, we follow a structured approach:

1. **Feature Request Submission**  
   Any new functionality or feature request should be submitted through the project's issue tracker.  
   Each request must include:
   - Detailed description
   - Use cases
   - Relevant references

2. **Prioritization and Planning**  
   Requests are reviewed and prioritized based on:
   - User demand
   - Project goals
   - Resource availability  
   Planning is done per sprint or release.

3. **Implementation**  
   Approved features are assigned to a developer or team and include:
   - Coding
   - Testing
   - Documentation

4. **Testing and Quality Assurance**  
   Each feature undergoes testing to ensure:
   - Functional correctness
   - No regressions or bugs

5. **Deployment**  
   Successfully tested features are deployed to production.  
   Users are informed via release notes or announcements.

6. **Feedback and Iteration**  
   User feedback is collected post-deployment and used for future improvements.

</details>

---

## 📂 Issues & Features Log

---

<details>
<summary><strong>🐞 Issue: User Session Persistence after Database Deletion</strong></summary>

**DATE:** 12/25/2025 – 11:45 PM  
**Development Team:** Startup team  
**Reported by:** Ahmad Al Dibo  
**Importance:** High  
**Category:** Bug & Improvement  
**Status:** Open  

**Slug:** `user-session-persistence-issue`

### Short Description
User sessions persist even after database deletion.

### Long Description
After deleting the database and restarting the server, the user remains logged in.  
Profile data persists because it is stored in the `request`, while user data is deleted since it is not stored there.

### Steps to Reproduce
1. Delete the database  
2. Restart the server  
3. Observe that the user remains logged in

### Expected Behavior
User should be logged out and all profile data should be cleared.

### Actual Behavior
User remains logged in and profile data persists.

### Suggested Fix
Clear user sessions and profile data from the `request` upon database deletion.
Create User session ID. so you do not need to save data in the request.
</details>

---

<details>
<summary><strong>🔗 Improvement: Use Slugs Instead of IDs in URLs</strong></summary>

**DATE:** 1/4/2026 – 9:33 PM  
**Development Team:** Startup team  
**Reported by:** Ahmad Al Dibo  
**Importance:** Medium  
**Category:** Improvement  
**Status:** Confirmed (1/5/2026 – 6:57 PM)  

**Slug:** `change-lesson-course-urls-to-slugs`

### Short Description
Update lesson and course URLs to use slugs for better readability.

### Long Description
Current URLs use integer IDs. These should be replaced with slugs for better readability and SEO.

**Examples:**
- Lesson:  
  `/lessons/<slug:course_slug>/<slug:lesson_slug>`
- Course:  
  `/courses/<slug:course_slug>`

Slug fields must be unique in `Lesson` and `Course` models.

### Steps to Reproduce
1. Access lesson or course via ID-based URL  
2. Update routing to use slugs  
3. Ensure slug uniqueness

### Expected Behavior
Readable, SEO-friendly URLs.

### Actual Behavior
URLs still use integer IDs.

### Suggested Fix
Update URL routing and enforce slug uniqueness.

</details>

---

<details>
<summary><strong>📝 Improvement: Show Only User-Created Lessons</strong></summary>

**DATE:** 12/30/2025 – 3:15 PM  
**Importance:** Low  
**Status:** Open  

**Slug:** `update-lessonform-to-display-user-lessons`

### Description
`LessonForm` in `user_lessons` view currently shows enrolled lessons.  
It should show **only lessons created by the logged-in user**.

Also add size validation for `lesson.thumbnail.url`.

### Suggested Fix
- Filter lessons by creator
- Add thumbnail size validation

</details>

---

<details>
<summary><strong>🖼️ Bug / Improvement: Lesson Thumbnail Size Validation</strong></summary>

**Dates:**  
- 12/28/2025 – Improvement  
- 12/27/2025 – Bug  

**Slugs:**  
- `add-size-validation-for-lesson-thumbnails`  
- `lesson-thumbnail-url-size-validation`

### Issue
Lesson thumbnail URLs have no size validation, causing display issues.

### Expected Behavior
Reject thumbnails that are too large or too small.

### Suggested Fix
Add size validation for `lesson.thumbnail.url`.

</details>

---

<details>
<summary><strong>🚨 Bug: Lesson Creation Fails Without Thumbnail Change</strong></summary>

**DATE:** 1/5/2026 – 6:20 PM  
**Importance:** High  
**Status:** Open  

**Slug:** `lesson-creation-redirect-issue`

### Description
Submitting the lesson form without changing the thumbnail:
- Returns HTTP 200
- Reloads form
- Does not save lesson

Changing the thumbnail allows submission.

### Suggested Fix
Fix validation and default handling for unchanged file fields.

</details>

---

<details>
<summary><strong>👤 Improvement: User Icon Not Displayed</strong></summary>

**DATE:** 1/5/2026 – 7:10 PM  
**Importance:** Medium  
**Status:** Open  

**Slug:** `user-icon-not-showing-in-lesson-view`

### Issue
User profile images are not shown in lesson views or author sections.

### Suggested Fix
Verify template image URLs and ensure images are accessible and rendered correctly.

</details>

---

<details>
<summary><strong>📝 Improvement: Add `your curses`</strong></summary>

**DATE:** 1/6/2026 – 8:54 PM  
**Importance:** High  
**Status:** Open  

**Slug:** `add-your-curses-to-profile-page`

### Issue
Add a section for "your curses" on the user profile page to display courses created by the user.
Add options to edit or delete these courses. ofcurse add a button to create a new course.

### Suggested Fix
Verify template image URLs and ensure images are accessible and rendered correctly.

</details>
