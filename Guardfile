guard :shell do
  watch(/^.*\.py$/) do |m|
    title = 'Test'
    eager "python #{m[1]}.py"
    status = ($?.success? && :success) || :failed
    n '', title, status
    ''
  end
end
