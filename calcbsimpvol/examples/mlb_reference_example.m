
% function mlb_reference_example()
    addpath('calcBSImpVol_mlab')
    
    file_path = fullfile('..' ,'data', 'reference_sample.json');
    fid = fopen(file_path, 'r');
    json_string = char(fread(fid))';
    fclose(fid);

    m = jsondecode(json_string);
    fn = 'd20170921';

    cp = m.(fn).cp;
    P = m.(fn).P;
    S = m.(fn).S(1);
    K = m.(fn).K;
    T = m.(fn).tau;
    r = m.(fn).r;
    q = m.(fn).q;

    limit = 100;
    elapsed = NaN(limit, 1);

    for i = 1 : limit
        tic
        
        [sigma, ~] = calcBSImpVol(cp, P, S, K, T, r, q);
        elapsed(i, 1) = toc;
    end

    fprintf('best run: %.2f ms\n', nanmin(elapsed)*1000)
    fprintf('best run per option : %.2f µs\n', nanmin(elapsed)/numel(sigma) * 1000 * 1000)
    rmpath('calcBSImpVol_mlab')

% end