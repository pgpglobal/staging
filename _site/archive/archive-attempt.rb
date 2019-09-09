# read dates into array
dates = []
datelist_path = File.expand_path("../../_site/archive/datelist.txt", __FILE__)
File.open(datelist_path, 'r') do |f|
  while date = f.gets
    date = date.strip
    dates += [{year: date[0..3], month: date[5..6], day: date[8..9]}]
    unless date == "" || date == "\n"
    end
  end

# create containing folders
dates_folder_path = File.expand_path("../dates/", __FILE__)
Dir.mkdir(dates_folder_path) unless File.exists?(dates_folder_path)

# create template files for each year and month
for date in dates
    # create year template files
    yearpage_path = dates_folder_path + "/#{date[:year]}.md"
    write_template_file(yearpage_path, "#{date[:year]}/", date[:year], {year:"#{date[:year]}"})

    # create month template files
    monthpage_path = dates_folder_path + "/#{date[:year]}-#{date[:month]}.md"
    month_name = "#{MONTH_NAMES[Integer(date[:month])]} #{date[:year]}"
    write_template_file(monthpage_path, "#{date[:year]}/#{date[:month]}/", month_name,
     {year: date[:year], month: date[:month]})
  end

  def write_template_file(path, permalink, title, options={})
    unless File.exists?(path)
      File.open(path, 'w') do |f|
        f.puts "---"
        f.puts "layout: archive"
        f.puts "permalink: '#{permalink}'"
        f.puts "title: '#{title}'"
        options.each do |k, v|
          f.puts "#{k}: '#{v}'"
        end
        f.puts "---"
      end
      puts "created archive page for #{title}"
    end
  end

