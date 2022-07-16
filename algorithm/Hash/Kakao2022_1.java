import java.util.*;

// 카카오 2022 블라인드 채용 [신고 결과 받기]
// https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=java

class Kakao2022_1 {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        // 1. report 중복 제거 => HashSet
        HashSet<String> reportSet = new HashSet<String>();
        for (String repo : report){
            reportSet.add(repo);
        }

        // 2. 신고받은 사람 목록 관리 => HashMap<String(신고받은 사람), ArrayList<String>(신고자들)>
        HashMap<String, ArrayList<String>> reporteeMap = new HashMap<>();
        for (String repo : reportSet){
            int blankIdx = repo.indexOf(" ");
            String reporter = repo.substring(0,blankIdx);
            String reportee = repo.substring(blankIdx+1);

            ArrayList<String> reporterList = reporteeMap.getOrDefault(reportee, new ArrayList<>());
            reporterList.add(reporter);

            reporteeMap.put(reportee, reporterList);
        }

        // 3. 메일 발송 대상자 관리 (size>=k) => HashMap<String(신고자 중 메일 발송 대상자), Integer(메일 발송 수)>
        HashMap<String,Integer> mailList = new HashMap<>();
        for (ArrayList<String> checkNotify : reporteeMap.values() ){
            if(checkNotify.size()>=k){
                for (String notifyReporter : checkNotify){
                    mailList.put(notifyReporter, mailList.getOrDefault(notifyReporter, 0)+1);
                }
            }
        }

        // 4. answer에 담기 => int[]
        for (int i=0;i< id_list.length; i++) {
            answer[i] = mailList.getOrDefault(id_list[i], 0);
        }
        return answer;
    }

    public static void main(String[] args) {
        Kakao2022_1 sol = new Kakao2022_1();
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        int k = 2;
        System.out.println(Arrays.toString(sol.solution(id_list, report, k)));
    }
}


/**
 * 다른 풀이 도전
 * @ HashSet 로직 합치기
 * @ .indexOf -> .split
 * @ LinkedHashMap (순서보장)
 * @ forEach
 * @ stream
 */

/*
public class Solution {

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        // 1. 신고받은 사람 목록 관리 => HashMap<String(신고받은 사람), HashSet<String>(신고자들 중복제거)>
        HashMap<String, HashSet<String>> reporteeMap = new HashMap<>();
        for (String repo : report){
            String reporter = repo.split(" ")[0];
            String reportee = repo.split(" ")[1];
            HashSet<String> reporterSet = reporteeMap.getOrDefault(reportee, new HashSet<>());
            reporterSet.add(reporter);

            reporteeMap.put(reportee, reporterSet);
        }

        // 2. 메일 발송 대상자 관리 (size>=k) => HashMap<String(신고자 중 메일 발송 대상자), Integer(메일 발송 수)>
        HashMap<String,Integer> mailList = new LinkedHashMap<>(); // 순서 보장

        for (String id : id_list){ // 이름 미리 순서대로 넣어두기 (->answer)
            mailList.put(id,0);
        }

        reporteeMap.forEach((key, value) ->{
            if(value.size()>=k){
                for (String v : value){
                    mailList.put(v, mailList.get(v)+1); // 이미 0 default
                }
            }
        });

        // 3. 정답 반환
        return mailList.values().stream().mapToInt(Integer::intValue).toArray();
    }

 */