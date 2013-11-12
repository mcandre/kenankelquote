guard :shell do
  watch('Gemfile') do |m|
    title = 'Bundler'
    msg = `bundle`
    status = ($?.success? && :success) || :failed

    n msg, title, status
    "-> #{msg}"
  end

  watch(/(.+)\.py/) do |m|
    title = 'Test'
    msg = `python #{m[1]}.py`
    status = ($?.success? && :success) || :failed

    n msg, title, status
    "-> #{msg}"
  end
end
