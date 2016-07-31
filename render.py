from exagogi import Exagogi
import os

def main():
	os.system('echo "markdown templates/md/resume/resume.md > templates/html/resume/body.html" ')
	os.system('markdown templates/md/resume/resume.md > templates/html/resume/body.html')
	
	base_path = 'templates/html/'
	base_output_path = 'output/'
	block = 'body'
	about = Exagogi(base_path + 'about/about.html', base_output_path + 'about.html', base_path + 'about/body.html',block)
	home = Exagogi(base_path + 'home/index.html', base_output_path + 'index.html', base_path + 'home/body.html', block)
	projects = Exagogi(base_path + 'projects/projects.html', base_output_path + 'projects.html', base_path + 'projects/body.html', block)
	resume = Exagogi(base_path + 'resume/resume.html', base_output_path + 'resume.html', base_path + 'resume/body.html',block)
	about.render()
	home.render()
	projects.render()
	resume.render()
main()